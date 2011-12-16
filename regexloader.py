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

from System.IO import StreamReader

clr.AddReference("System.Xml")

from System.Xml import XmlDocument

from common import ImageRegex, LinkRegex, SiteRegex



def load_regex_from_file(regex_file):
    """Loads the regex from the specified xml file"""

    file = StreamReader(regex_file)
    xml = XmlDocument()
    xml.Load(file)
    file.Close()


    nodes = xml.SelectNodes("WebComicHelper/ImageRegex")

    images = []

    for node in nodes:

        images.append(ImageRegex(node.InnerText))

    nodes = xml.SelectNodes("WebComicHelper/LinkRegex")

    links = []

    for node in nodes:

        links.append(LinkRegex(node.InnerText))


    nodes = xml.SelectNodes("WebComicHelper/Site")

    sites = []

    for node in nodes:

        sites.append(SiteRegex(node.SelectSingleNode("ImageRegex").InnerText, node.SelectSingleNode("LinkRegex").InnerText, node.SelectSingleNode("Domain").InnerText))


    return images, links, sites
    
