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

clr.AddReference("System.Xml")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System import Convert

from System.Xml import XmlWriter, XmlWriterSettings

from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon

from System.IO import FileInfo, Path

from System.Drawing import Color, ColorTranslator

SCIRPT_DIRECTORY = FileInfo(__file__).DirectoryName

REGEX_FILE = Path.Combine(SCIRPT_DIRECTORY, "regex.dat")

ICON = Path.Combine(SCIRPT_DIRECTORY, "webcomichelper.ico")

HEADER_IMAGE = Path.Combine(SCIRPT_DIRECTORY, "Webcomic Helper.png")


class WebComicHelperResult(object):

    def __init__(self, result, imageregex = None, linkregex = None):
        
        self._result = result
        self._image_regex = imageregex
        self._link_regex = linkregex


class WebComicHelperResultEnum(object):
    NoImages = 1
    NoLinks = 2
    Site = 3
    Success = 4



class LinkRegex(object):
        
    def __init__(self, regex):
        self._regex = regex
        self._matches = 0



class ImageRegex(object):
        
    def __init__(self, regex):
        self._regex = regex
        self._matches = 0



class SiteRegex(object):
        
    def __init__(self, imageregex, linkregex, domain):
        self._image_regex = imageregex
        self._link_regex = linkregex
        self._domain = domain



class NextPageLinkFormResult(object):
    def __init__(self, text, isimage):
        self.is_image = isimage
        self.text = text



class WebComic(object):

    def __init__(self, info, compositing, starturl, helper_result):
        """Info should be a dict of all the info"""
        self._info = info
        self._compositing = compositing
        self._start_url = starturl
        self._image_regex = helper_result._image_regex
        self._link_regex = helper_result._link_regex

    def SaveToXml(self, filepath):
        """Saves the cbw file to the filepath
        filepath should be the complete path to a cbw file
        """
        xsettings = XmlWriterSettings()
        xsettings.Indent = True
        try:
            xmlwriter = XmlWriter.Create(filepath, xsettings)

        except (System.UnauthorizedAccessException, System.IO.IOException), ex:
            MessageBox.Show("An error occured trying to create the cbw file. The error was:\n\n" + ex.Message + "\n\nTry again with a different file path", 
                            "Could not create cbw", MessageBoxButtons.OK, MessageBoxIcon.Error)
            return False

        with xmlwriter:
            xmlwriter.WriteStartElement("WebComic")
            self._write_info(xmlwriter)
            self._compositing.write_to_xml(xmlwriter)
            self._write_regex(xmlwriter)
            xmlwriter.WriteEndElement()

        return True

    def _write_info(self, xmlwriter):
        """Writes the info portion of the cbw using the passed xmlwriter"""
        xmlwriter.WriteStartElement("Info")
        for item in self._info:
            xmlwriter.WriteElementString(item, self._info[item])
        xmlwriter.WriteEndElement()


    def _write_regex(self, xmlwriter):
        """Writes the regex portion of the cbw using the passed xmlwriter"""

        xmlwriter.WriteStartElement("Images")
        xmlwriter.WriteStartElement("Image")
        xmlwriter.WriteAttributeString("Url", "?" + self._start_url)
        xmlwriter.WriteStartElement("Parts")
        xmlwriter.WriteElementString("Part", self._image_regex)
        xmlwriter.WriteElementString("Part", self._link_regex)
        xmlwriter.WriteEndElement()
        xmlwriter.WriteEndElement()
        xmlwriter.WriteEndElement()



class WebComicCompositing(object):
    
    def __init__(self, use_rows_and_columns, value1, value2, color, border, right_to_left):
        """
        use_rows_and_columns is a bool. True if using columns, False if using height and width.
        value1 is the rows or height.
        value2 is the columns or width.
        color is the background color to use.
        border is the borderwidth to use.
        """
        self._use_rows_and_columns = use_rows_and_columns
        self._value1 = value1
        self._value2 = value2
        self._color = color
        self._border_width = border
        self._right_to_left = right_to_left == "Yes"


    def write_to_xml(self, xmlwriter):
        xmlwriter.WriteStartElement("Compositing")
        if self._use_rows_and_columns and self._value1 > 1 and self._value2 > 1:
            xmlwriter.WriteAttributeString("Rows", str(self._value1))
            xmlwriter.WriteAttributeString("Columns", str(self._value2))
        elif not self._use_rows_and_columns:
            xmlwriter.WriteAttributeString("PageHeight", str(self._value1))
            xmlwriter.WriteAttributeString("PageWidth", str(self._value2))
        if self._right_to_left:
            #Rather oddly ComicRack only loads right to left if the bool is in lower case.
            xmlwriter.WriteAttributeString("RightToLeft", str(self._right_to_left).lower())
        xmlwriter.WriteAttributeString("BorderWidth", str(self._border_width))
        if self._color != Color.White:
            xmlwriter.WriteAttributeString("BackgroundColor", ColorTranslator.ToHtml(self._color))

        xmlwriter.WriteEndElement()