"""
Copyright 2011 Stonepaw & Helmic

This file is part of Webcomic Helper.

Webcomic Helper is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Webcomic Helper is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Webcomic Helper. If not, see <http://www.gnu.org/licenses/>.
"""

import clr

import System

import regexloader

from System import Func, ArgumentNullException, UriFormatException, Uri

clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import DialogResult

clr.AddReference("System.Net")

from System.Net import HttpWebRequest, WebException, ProtocolViolationException

from System.IO import StreamReader
    
from System.Text.RegularExpressions import RegexOptions, Regex

from common import LinkRegex, ImageRegex, WebComicHelperResult, WebComicHelperResultEnum, NextPageLinkFormResult, REGEX_FILE

debug = True
print_source = False

debug_backup_regex = False

import wizard

#@Name Webcomic Helper
#@Hook Books, Library
#@Image webcomichelper.png
def WebComicHelper(books):
    
    wizard.ComicRack = ComicRack

    f = wizard.WebComicHelperWizard()
    r = f.ShowDialog()

    opencomic = f._open_webcomic.Checked

    if r != DialogResult.Cancel:
        if opencomic:
            ComicRack.App.OpenBooks.Open(f.book, 0, 0)

    f.Dispose()

    

def webcomic_helper_do_work(worker, e):
    
    form = e.Argument["Form"]

    if debug: print "Loading regex from file"
    worker.ReportProgress(0, "Loading regex from file")
    images_regex, links_regex, sites = regexloader.load_regex_from_file(REGEX_FILE)

    if debug_backup_regex:
        images_regex = []
        links_regex = []

    #Load the variables passed from the form. It should be in the form of a dict
    first_page_url = e.Argument["FirstPage"]
    image_url = e.Argument["Image"]
    second_page_url = e.Argument["SecondPage"]

    if worker.CancellationPending:
        e.Cancel = True
        return

    try:
        global first_page_uri
        global second_page_uri
        first_page_uri = System.Uri(first_page_url)
        second_page_uri = System.Uri(second_page_url)

        global escaped_first_page_uri
        global escaped_second_page_uri

        escaped_first_page_uri = System.Uri(escape_uri_string(first_page_uri))
        escaped_second_page_uri = System.Uri(escape_uri_string(second_page_uri))

        escaped_image_url = escape_uri_string(image_url)

        if debug:
            print first_page_uri.AbsoluteUri
            print second_page_uri.AbsoluteUri
            print escaped_first_page_uri.AbsoluteUri
            print escaped_second_page_uri.AbsoluteUri
            print image_url
            print escaped_image_url
            

    except UriFormatException, ex:
        #Errored occured. Raise an error to exit the background thread
        raise UriFormatException(ex.Message, ex)

    except ArgumentNullException, ex:
        raise ArgumentNullException(ex.Message, ex)


    if debug: print "Checking if the input url is a defined site"
    #Check if the site domain is in the list of sites
    for site in sites:
        if site._domain == first_page_uri.Host:
            if debug: print first_page_uri.Host + " is a defined site"
            e.Result = WebComicHelperResult(WebComicHelperResultEnum.Site, site._image_regex, site._link_regex)
            return


    #Get the page sources
    
    #Get the source from the first page
    if debug: print "Getting first page source"
    worker.ReportProgress(1, "Retrieving first page source")

    if worker.CancellationPending:
        e.Cancel = True
        return
        
    global first_page_source

    first_page_source = PageSource()
    result = first_page_source.get_source(first_page_uri)

    if result == False:
        raise System.Exception(first_page_source._exception.Message, first_page_source._exception)

    if print_source: print first_page_source._source
    
    #Get the source from the second page
    worker.ReportProgress(2, "Retrieving second page source")

    
    if debug: print "Getting second page source"

    if worker.CancellationPending:
        e.Cancel = True
        return

    global second_page_source
    second_page_source = PageSource()
    result = second_page_source.get_source(second_page_uri)

    if result == False:
        raise System.Exception(second_page_source._exception.Message, second_page_source._exception)


    if print_source: print second_page_source._source

    #Try and find a image regex that works on both pages.

    #Move this stuff to another method since it is pretty much the same for both link and image
    worker.ReportProgress(3, "Searching for matching regex")

    valid_image_regex = []

    if debug: print "\n\nStarting to search for image regex"

    for imageregex in images_regex:

        if worker.CancellationPending:
            e.Cancel = True
            return

        result = check_regex_against_source(imageregex, image_url, escaped_image_url)

        if result:
            valid_image_regex.append(result)
                    
    
    #If no valid image regex
    if len(valid_image_regex) == 0:

        if debug: print "No Valid image regex found"

        #Try and get the url of the image on the second page from the user
        second_image_url = form.Invoke(Func[str](form.get_second_image_url))

        #User canceled the inputing the second image url
        if second_image_url == "":
            e.Result = WebComicHelperResult(WebComicHelperResultEnum.NoImages)
            return

        #Try and create a image regex
        image_regex = create_image_regex(image_url, second_image_url)

        #couldn't create a image regex
        if image_regex is None:
            e.Result = WebComicHelperResult(WebComicHelperResultEnum.NoImages)
            return

        valid_image_regex.append(image_regex)
                
                
                    


    #Now try and find a link regex that works on both pages

    if debug: print "\n\n\nFinding a next page link regular expression"

    valid_link_regex = []

    for linkregex in links_regex:

        if worker.CancellationPending:
            e.Cancel = True
            return

        result = check_regex_against_source(linkregex, second_page_uri.AbsoluteUri, escaped_second_page_uri.AbsoluteUri)

        if result:
            valid_link_regex.append(result)
                    
    
    if len(valid_link_regex) == 0:
        
        if debug: print "No valid link regex could be found"

        next_page_link_result = form.Invoke(Func[NextPageLinkFormResult](form.get_next_page_link))

        if next_page_link_result.text == "":
            e.Result = WebComicHelperResult(WebComicHelperResultEnum.NoLinks)
            return

        if next_page_link_result.is_image:
            link_regex = create_next_link_regx_with_image(next_page_link_result.text)

        else:
            link_regex = create_next_link_regx_with_text(next_page_link_result.text)

        if link_regex is None:
            e.Result = WebComicHelperResult(WebComicHelperResultEnum.NoLinks)
            return

        valid_link_regex.append(link_regex)


    #If the script gets this far there should be at least one valid image regex and one valid link regex
    
    return_image_regex = get_best_regex(valid_image_regex, "Image")
    return_link_regex = get_best_regex(valid_link_regex, "Link")


    worker.ReportProgress(4, "Done")
    e.Result = WebComicHelperResult(WebComicHelperResultEnum.Success, return_image_regex, return_link_regex)

    if worker.CancellationPending:
        e.Cancel = True

    return


def check_regex_against_source(regex, check_value, check_value2):

    matches = Regex.Matches(first_page_source._source, regex._regex, RegexOptions.IgnoreCase)

    if matches.Count != 0:

        if debug:
            print "\n\nFound " + str(matches.Count) + " match(es) on the first page with regex: " + regex._regex
            print "Captured: " + matches[0].Value
            print "link group: " + matches[0].Groups["link"].Value

        #We don't care if there is more than one result. As long as the first result is the correct image
        result, result_uri = Uri.TryCreate(first_page_uri, matches[0].Groups["link"].Value)
        
        
        if result and result_uri.AbsoluteUri in (check_value, check_value2):

            #Valid url and matches against the check_value

            if debug: print "Valid uri"

        else:
            return False

        matches_second = Regex.Matches(second_page_source._source, regex._regex, RegexOptions.IgnoreCase)

        if matches_second.Count == 0:
            if debug: print "No matches found on the second page"
            return False

        #Regex match on the second page. Same deal as above. We don't care if there is more than one result

        if debug:
            print "\nFound " + str(matches_second.Count) + " match(es) on the second page"
            print "Captured: " + matches_second[0].Value
            print "link group: " + matches_second[0].Groups["link"].Value

        result, result_uri = Uri.TryCreate(second_page_uri, matches_second[0].Groups["link"].Value)

        if result:
            regex._matches = matches.Count
            if debug: print "Added to valid regex"
            return regex

        else:
            if debug: print "Invalid uri"
            return False

    return False


def get_best_regex(regex_list, name = ""):

    return_regex = ""

    if len(regex_list) > 1:
        #More than one valid regex so try and choose the best one.
        number = 0
        #try and get the one with the least amount of matches
        for regex in regex_list:
            if number == 0 or regex._matches < number:
                number = regex._matches
                return_regex = regex._regex

        if debug: print "\n\n" + name + " regex being used is : " + return_regex + "\nand has " +  str(number) + " matches per page"

    else:
        return_regex = regex_list[0]._regex
        if debug: print "\n\n" + name + " regex being used is : " + return_regex + "\nand has " +  str(regex_list[0]._matches) + " matches per page"


    return return_regex


def create_image_regex(first_image_url, second_image_url):

    if debug: print "Starting to create an image regex with urls:\n" + first_image_url + "\n" + second_image_url

    base = get_string_intersect(first_image_url, second_image_url)

    baseuri = Uri(base)

    
    relativeuri = first_page_uri.MakeRelativeUri(baseuri)

    if relativeuri.IsAbsoluteUri:
        domain = relativeuri.Scheme + "://" + relativeuri.Host
        relative = relativeuri.AbsolutePath
    
    else:
        domain = baseuri.Scheme + "://" + baseuri.Host
        relative = relativeuri.OriginalString

    domain = escape_regex_characters(domain)

    relative = relative.lstrip("/")

    relative = escape_regex_characters(relative)

    relative = replace_date_values(relative)

    domain = Regex.Replace(domain, "www\\\\.", "(?:www\\.)?", RegexOptions.IgnoreCase)

    baseregex = "(?:" + domain + ")?\\.*/?" + relative

    if debug: print "baseregex is: " + baseregex

    regex = "src\\s*=\\s*(?([\"'])[\"'](?<link>" + baseregex + "[^\"']+)[\"']|(?<link>" + baseregex + "[^\\s<>]+))"

    result, matches = check_created_image_regex(first_image_url, second_image_url, regex)

    if not result:

        regex = "(?([\"'])[\"'](?<link>" + baseregex + "[^\"']+)[\"']|(?<link>" + baseregex + "[^\\s<>]+))"

        result, matches = check_created_image_regex(first_image_url, second_image_url, regex)

        if not result:
            #Sometimes the relative link creator makes a bad split, in that case try one other way:
            #Check if we made the split before:
            if baseuri.Host == first_page_uri.Host:

                domain = baseuri.Scheme + "://" + baseuri.Host
                relative = baseuri.AbsolutePath

                relative = relative.lstrip("/")

                domain = escape_regex_characters(domain)

                relative = escape_regex_characters(relative)

                relative = replace_date_values(relative)

                domain = Regex.Replace(domain, "www\\\\.", "(?:www\\.)?", RegexOptions.IgnoreCase)

                baseregex = "(?:" + domain + ")?\\.*/?" + relative

                if debug: print "baseregex is: " + baseregex

                regex = "src\\s*=\\s*(?([\"'])[\"'](?<link>" + baseregex + "[^\"']+)[\"']|(?<link>" + baseregex + "[^\\s<>]+))"

                result, matches = check_created_image_regex(first_image_url, second_image_url, regex)

                if not result:
                    regex = "(?([\"'])[\"'](?<link>" + baseregex + "[^\"']+)[\"']|(?<link>" + baseregex + "[^\\s<>]+))"

                    result, matches = check_created_image_regex(first_image_url, second_image_url, regex)

                    if not result:

                        if debug:  print "Unable create a working image regex"          
                        return None

    if debug: print "Found a working image regex: " + regex
    imgregex = ImageRegex(regex)
    imgregex._matches = matches
    return imgregex


def replace_date_values(string):
    string = Regex.Replace(string, r"(?<=/)\d+(?=/)", r"(?<=/)\d+(?=/)", RegexOptions.IgnoreCase)
    string = Regex.Replace(string, r"(?<=/)(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)(?=/)",
                                   r"(?<=/)(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)(?=/)", RegexOptions.IgnoreCase)

    return string


def escape_uri_string(uri):
    if type(uri) != System.Uri:
        uri = Uri(uri)
    string = uri.AbsolutePath
    for character in ["%", "!", "*", "'", "(", ")", ";", ":", "@", "&", "=", "+", "$", ",", "?", "#", "[", "]", " "]:
        string = string.replace(character, Uri.HexEscape(character))

    return uri.Scheme + "://" + uri.Host + string


def check_created_image_regex(first_image_url, second_image_url, regex):
    matches = Regex.Matches(first_page_source._source, regex, RegexOptions.IgnoreCase)

    escaped_first_image_url = escape_uri_string(first_image_url)
    escaped_second_image_url = escape_uri_string(second_image_url)

    if matches.Count == 0:
        return False, 0
    else:
        if debug:
            print "\nFound " + str(matches.Count) + " match(es) on the first page with regex: " + regex
            print "Captured: " + matches[0].Value
            print "link group: " + matches[0].Groups["link"].Value

        #We don't care if there is more than one result. As long as the first result is the correct image
        result, image_uri = Uri.TryCreate(first_page_uri, matches[0].Groups["link"].Value)
            
        #Valid url and matches the input image url
        if result and image_uri.AbsoluteUri in (first_image_url, escaped_first_image_url):
            if debug: print "Valid uri and matches image url"

        else:
            if debug: print "Not a valid uri or doesn't match image url"
            return False, 0

        matches_second = Regex.Matches(second_page_source._source, regex, RegexOptions.IgnoreCase)

        if matches_second.Count == 0:
            if debug: print "No matches on the second page"
            return False, 0

        #Regex match on the second page. Same deal as above. We don't care if there is more than one result
        if debug:
            print "\nFound " + str(matches_second.Count) + " match(es) on the second page"
            print "Captured: " + matches_second[0].Value
            print "link group: " + matches_second[0].Groups["link"].Value

        result, image_uri = Uri.TryCreate(second_page_uri, matches_second[0].Groups["link"].Value)

        if result and image_uri.AbsoluteUri in (second_image_url, escaped_second_image_url):
                        
            if debug: print "Regex works on both pages and returns the correct image"
            return True, matches.Count

        else:
            if debug: print "Invalid Uri or doesn't match the second image url"
            return False, 0

    return False, matches.Count


def escape_regex_characters(string):
    #TODO:Replace with System.Text.RegualrExpressions.Regex.Escape
    string = string.replace("\\", "\\\\")
    string = string.replace("^", "\\^")
    string = string.replace("$", "\\$")
    string = string.replace(".", "\\.")
    string = string.replace("|", "\\|")
    string = string.replace("{", "\\{")
    string = string.replace("}", "\\}")
    string = string.replace("[", "\\[")
    string = string.replace("]", "\\]")
    string = string.replace("(", "\\(")
    string = string.replace(")", "\\)")
    string = string.replace("*", "\\*")
    string = string.replace("+", "\\+")
    string = string.replace("?", "\\?")

    return string


def create_next_link_regx_with_image(next_link_image_url):
    """Creates a link regex using the image behind the next link"""

    if debug: print "Trying to create a next page link regex with image url:\n" + next_link_image_url

    next_link_url_escaped = escape_regex_characters(next_link_image_url)
    
    regex = "<a\\s[^<>]*href\\s*=\\s*(?([\"'])[\"'](?<link>[^\"']+)[\"']|(?<link>[^\\s<>]+))[^<>]*>[\\s\\n\\r\\t]*<img\\s[^<>]*src\\s*=\\s*[\"']?" + next_link_url_escaped + "[\"']?"

    result, matches = check_created_link_regex(regex)

    if not result:
        
        #Try with a relative link:

        relative_next_link_url = first_page_uri.MakeRelativeUri(Uri(next_link_image_url)).OriginalString

        if debug: print "Trying with relative image url: " + relative_next_link_url

        relative_next_link_url = relative_next_link_url.lstrip("/")

        relative_next_link_url = escape_regex_characters(relative_next_link_url)



        regex = "<a\\s[^<>]*href\\s*=\\s*(?([\"'])[\"'](?<link>[^\"']+)[\"']|(?<link>[^\\s<>]+))[^<>]*>[\\s\\n\\r\\t]*<img\\s[^<>]*src\\s*=\\s*[\"']?\\.*/?" + relative_next_link_url + "[\"']?"

        result, matches = check_created_link_regex(regex)

        if not result:
            
            #Try one other way

            relative_next_link_url = Uri(next_link_image_url).AbsolutePath

            relative_next_link_url = relative_next_link_url.lstrip("/")

            relative_next_link_url = escape_regex_characters(relative_next_link_url)

            if debug: print "Trying with relative image url: " + relative_next_link_url

            regex = "<a\\s[^<>]*href\\s*=\\s*(?([\"'])[\"'](?<link>[^\"']+)[\"']|(?<link>[^\\s<>]+))[^<>]*>[\\s\\n\\r\\t]*<img\\s[^<>]*src\\s*=\\s*[\"']?\\.*/?" + relative_next_link_url + "[\"']?"

            result, matches = check_created_link_regex(regex)

            if not result:
                if debug: print "Couldn't create a next page regex with the image url"
                return None

    if debug: print "Found a next page regex with the image url!"
    link = LinkRegex(regex)
    link._matches = matches

    return link


def create_next_link_regx_with_text(text):
    """Creates a link regex using the image behind the next link"""

    if debug: print "Trying to create a next page link regex with text:\n" + text

    text = escape_regex_characters(text)
    
    regex = "<a\\s[^<>]*?href\\s*=\\s*(?(['\"])[\"'](?<link>[^\"']+)[\"']|(?<link>[^\\s<>]+))[^<>]*?>[\\s\\n\\r\\t]*" + text + "[\\s\\n\\r\\t]*</a"

    result, matches = check_created_link_regex(regex)

    if not result:
        if debug: print "Couldn't create a next page regex with the text"
        return None

    if debug: print "Found a next page regex with the text!"
    link = LinkRegex(regex)
    link._matches = matches

    return link


def create_next_link_regex_from_css_attribute(third_page_url):
    """
    Creates a next link regex by trying to find the closest css id or class and using that to find the page link.

    third_page_url->The url of the third comic page
    """
    if debug: print "Trying to create a next page link regex with css attributes:\n"

    #First try and find the class or id for the link

    #First we need the realtive url of the second page
    relative_second_page_url = first_page_uri.MakeRealtiveUri(second_page_uri).OriginalString

    relative_second_page_url = relative_second_page_url.lstrip("/")

    relative_second_page_url = Regex.Escape(relative_second_page_url)

    if debug: print "Trying to find the class/id with relative url: %s" % (relative_second_page_url)

    regex = "href\\s?=\\s?\"?/?" + relative_second_page_url + ".*?(?<class>(?:id|class)\\s?=\\s?(?(['\"])[\"'][^\"']+[\"']|[^\\s<>]+))"


def check_created_link_regex(regex):
    matches = Regex.Matches(first_page_source._source, regex, RegexOptions.IgnoreCase)

    if matches.Count == 0:
        return False, 0
    else:
        if debug:
            print "\nFound " + str(matches.Count) + " match(es) on the first page with regex: " + regex
            print "Captured: " + matches[0].Value
            print "link group: " + matches[0].Groups["link"].Value

        #We don't care if there is more than one result. As long as the first result is the correct image
        result, link_uri = Uri.TryCreate(first_page_uri, matches[0].Groups["link"].Value)
            
        #Valid url and matches the input image url
        if result and link_uri.AbsoluteUri in (second_page_uri.AbsoluteUri, escaped_second_page_uri.AbsoluteUri):
            if debug: print "Valid uri and matches the second page url"

        else:
            if debug: print "Invalid uri or doesn't match the second page url"
            return False, 0

        matches_second = Regex.Matches(second_page_source._source, regex, RegexOptions.IgnoreCase)

        if matches_second.Count == 0:
            if debug: print "\nNo matches on the second page"
            return False, 0

        #Regex match on the second page. Same deal as above. We don't care if there is more than one result
        if debug:
            print "\nFound " + str(matches_second.Count) + " match(es) on the second page"
            print "Captured: " + matches_second[0].Value
            print "link group: " + matches_second[0].Groups["link"].Value

        result, link_uri = Uri.TryCreate(second_page_uri, matches_second[0].Groups["link"].Value)

        if result:
                                    
            if debug: print "Regex works on both pages"
            return True, matches.Count

        else:
            if debug: print "Invalid uri"

    return False, matches.Count


def get_string_intersect(string1, string2):
    #There is probably an easier way to do this but I can't find one at 2 in the morning :p
    s1 = list(string1)
    s2 = list(string2)
    r = []
    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            r.append(s1[i])
        else:
            break
    
    #Because the base needs to end in /
    r.reverse()
    for i in r[:]:
        if i != "/":
            r.remove(i)

        else:
            break

    r.reverse()

    return "".join(r)


class PageSource(object):
    """PageSource is a class containing methods to get the page source from a website"""

    def __init__(self):

        self._source = ""

        self._exception = None


    def get_source(self, URI):
        """URI should be a valid URI instance"""

        success = True

        try:

            request = HttpWebRequest.Create(URI)
            request.UserAgent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"

        except (ArgumentNullException, System.Security.SecurityException), ex:

            self._exception = ex
            return False

        try:
            responsestream = request.GetResponse()

        except (System.Security.SecurityException, WebException), ex:

            self._exception = ex
            return False

        try:

            streamreader = StreamReader(responsestream.GetResponseStream())

            self._source = streamreader.ReadToEnd()

        except (ArgumentException, ProtocolViolationException), ex:

            self._exception = ex
            success = False

        finally:
            responsestream.Close()
            streamreader.Close()

            return success

