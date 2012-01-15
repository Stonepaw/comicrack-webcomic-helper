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

clr.AddReferenceByPartialName("Controls")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

import CristiPotlog.Controls

import System.Drawing
import System.Windows.Forms

from System.ComponentModel import BackgroundWorker

from System.Drawing import *
from System.Windows.Forms import *

import webcomichelper

from common import WebComicHelperResultEnum, NextPageLinkFormResult, WebComic, HEADER_IMAGE, WebComicCompositing

from forms import NextPageLink, SecondImageUrl

class WebComicHelperWizard(Form):


    def __init__(self):
        self.InitializeComponent()

        self._info_textboxes = [self._Writer, self._Penciler, self._Inker, self._Colorist, self._Summary]

    
    def InitializeComponent(self):
        self._wizard = CristiPotlog.Controls.Wizard()
        self._wpURL = CristiPotlog.Controls.WizardPage()
        self._label1 = System.Windows.Forms.Label()
        self._firstPageUrl = System.Windows.Forms.TextBox()
        self._wpInfo = CristiPotlog.Controls.WizardPage()
        self._webcomic_name = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._Writer = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._Penciler = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._Summary = System.Windows.Forms.TextBox()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._Inker = System.Windows.Forms.TextBox()
        self._Colorist = System.Windows.Forms.TextBox()
        self._label11 = System.Windows.Forms.Label()
        self._Manga = System.Windows.Forms.ComboBox()
        self._label10 = System.Windows.Forms.Label()
        self._BlackAndWhite = System.Windows.Forms.ComboBox()
        self._save_file_dialog = System.Windows.Forms.SaveFileDialog()
        self._wpFinished = CristiPotlog.Controls.WizardPage()
        self._label13 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._imageUrl = System.Windows.Forms.TextBox()
        self._linkUrl = System.Windows.Forms.TextBox()
        self._wpFailedImage = CristiPotlog.Controls.WizardPage()
        self._wpFaliedLink = CristiPotlog.Controls.WizardPage()
        self._wpProgress = CristiPotlog.Controls.WizardPage()
        self._ProgressBar = System.Windows.Forms.ProgressBar()
        self._ProgressText = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._background_worker = BackgroundWorker()
        self._open_webcomic = System.Windows.Forms.CheckBox()
        self._wpCompositing = CristiPotlog.Controls.WizardPage()
        self._use_columns_and_rows = System.Windows.Forms.RadioButton()
        self._use_height_and_width = System.Windows.Forms.RadioButton()
        self._columns = System.Windows.Forms.NumericUpDown()
        self._color_dialog = System.Windows.Forms.ColorDialog()
        self._rows = System.Windows.Forms.NumericUpDown()
        self._height = System.Windows.Forms.NumericUpDown()
        self._width = System.Windows.Forms.NumericUpDown()
        self._colums_label = System.Windows.Forms.Label()
        self._rows_label = System.Windows.Forms.Label()
        self._height_label = System.Windows.Forms.Label()
        self._width_label = System.Windows.Forms.Label()
        self._background_color_button = System.Windows.Forms.Button()
        self._background_color_preview = System.Windows.Forms.Panel()
        self._border_width_label = System.Windows.Forms.Label()
        self._right_to_left_label = System.Windows.Forms.Label()
        self._background_color_label = System.Windows.Forms.Label()
        self._right_to_left = System.Windows.Forms.ComboBox()
        self._border_width = System.Windows.Forms.NumericUpDown()
        self._wizard.SuspendLayout()
        self._wpURL.SuspendLayout()
        self._wpInfo.SuspendLayout()
        self._wpFailedImage.SuspendLayout()
        self._wpFaliedLink.SuspendLayout()
        self._wpProgress.SuspendLayout()
        self._wpCompositing.SuspendLayout()
        self._columns.BeginInit()
        self._rows.BeginInit()
        self._height.BeginInit()
        self._width.BeginInit()
        self._border_width.BeginInit()
        self.SuspendLayout()
        # 
        # wizard
        # 
        self._wizard.Controls.Add(self._wpFaliedLink)
        self._wizard.Controls.Add(self._wpFailedImage)
        self._wizard.Controls.Add(self._wpFinished)
        self._wizard.Controls.Add(self._wpInfo)
        self._wizard.Controls.Add(self._wpProgress)
        self._wizard.Controls.Add(self._wpURL)
        self._wizard.Controls.Add(self._wpCompositing)
        self._wizard.Location = System.Drawing.Point(0, 0)
        self._wizard.HeaderImage = Image.FromFile(HEADER_IMAGE)
        self._wizard.Pages.AddRange(System.Array[CristiPotlog.Controls.WizardPage](
            [self._wpURL,
            self._wpProgress,
            self._wpInfo,
            self._wpCompositing,
            self._wpFinished,
            self._wpFailedImage,
            self._wpFaliedLink]))
        self._wizard.Size = System.Drawing.Size(531, 414)
        self._wizard.TabIndex = 0
        self._wizard.BeforeSwitchPages += self.before_switch_page
        self._wizard.AfterSwitchPages += self.after_switch_page
        self._wizard.Cancel += self.wizard_cancel
        # 
        # wpURL
        # 
        self._wpURL.Controls.Add(self._linkUrl)
        self._wpURL.Controls.Add(self._imageUrl)
        self._wpURL.Controls.Add(self._firstPageUrl)
        self._wpURL.Controls.Add(self._label19)
        self._wpURL.Controls.Add(self._label17)
        self._wpURL.Controls.Add(self._label16)     
        self._wpURL.Controls.Add(self._label18)
        self._wpURL.Controls.Add(self._label13)     
        self._wpURL.Controls.Add(self._label1)
        self._wpURL.Description = "Enter the URLs of the first webcomic page, the image on that page and the URL of the second page"
        self._wpURL.Location = System.Drawing.Point(0, 0)
        self._wpURL.Name = "wpURL"
        self._wpURL.Size = System.Drawing.Size(531, 366)
        self._wpURL.TabIndex = 10
        self._wpURL.Title = "First Page URLs"
        # 
        # label1
        # 
        self._label1.AutoSize = True
        self._label1.Location = System.Drawing.Point(12, 88)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(82, 13)
        self._label1.TabIndex = 0
        self._label1.Text = "First Page URL:"
        # 
        # firstPageUrl
        # 
        self._firstPageUrl.Location = System.Drawing.Point(111, 85)
        self._firstPageUrl.Name = "firstPageUrl"
        self._firstPageUrl.Size = System.Drawing.Size(408, 20)
        self._firstPageUrl.TabIndex = 1
        # 
        # wpInfo
        # 
        self._wpInfo.Controls.Add(self._BlackAndWhite)
        self._wpInfo.Controls.Add(self._label10)
        self._wpInfo.Controls.Add(self._Manga)
        self._wpInfo.Controls.Add(self._label11)
        self._wpInfo.Controls.Add(self._Colorist)
        self._wpInfo.Controls.Add(self._Inker)
        self._wpInfo.Controls.Add(self._label9)
        self._wpInfo.Controls.Add(self._label8)
        self._wpInfo.Controls.Add(self._Summary)
        self._wpInfo.Controls.Add(self._label7)
        self._wpInfo.Controls.Add(self._Penciler)
        self._wpInfo.Controls.Add(self._label6)
        self._wpInfo.Controls.Add(self._Writer)
        self._wpInfo.Controls.Add(self._label4)
        self._wpInfo.Controls.Add(self._label3)
        self._wpInfo.Controls.Add(self._webcomic_name)
        self._wpInfo.Description = "Enter any desired information"
        self._wpInfo.Location = System.Drawing.Point(0, 0)
        self._wpInfo.Name = "wpInfo"
        self._wpInfo.Size = System.Drawing.Size(531, 366)
        self._wpInfo.TabIndex = 13
        self._wpInfo.Title = "Comic Information"
        # 
        # SeriesName
        # 
        self._webcomic_name.Location = System.Drawing.Point(110, 80)
        self._webcomic_name.Size = System.Drawing.Size(408, 20)
        self._webcomic_name.TabIndex = 0
        # 
        # label3
        # 
        self._label3.AutoSize = True
        self._label3.Location = System.Drawing.Point(12, 83)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(92, 13)
        self._label3.Text = "Webcomic Name:"
        # 
        # label4
        # 
        self._label4.AutoSize = True
        self._label4.Location = System.Drawing.Point(12, 147)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(38, 13)
        self._label4.Text = "Writer:"
        # 
        # Writer
        # 
        self._Writer.Location = System.Drawing.Point(56, 143)
        self._Writer.Name = "Writer"
        self._Writer.Size = System.Drawing.Size(140, 20)
        self._Writer.TabIndex = 1
        self._Writer.Tag = "Writer"
        # 
        # label6
        # 
        self._label6.AutoSize = True
        self._label6.Location = System.Drawing.Point(258, 175)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(44, 13)
        self._label6.Text = "Colorist:"
        # 
        # Penciler
        # 
        self._Penciler.Location = System.Drawing.Point(312, 143)
        self._Penciler.Name = "Penciler"
        self._Penciler.Size = System.Drawing.Size(139, 20)
        self._Penciler.TabIndex = 2
        self._Penciler.Tag = "Penciller"
        # 
        # label7
        # 
        self._label7.AutoSize = True
        self._label7.Location = System.Drawing.Point(12, 256)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(53, 13)
        self._label7.Text = "Summary:"
        # 
        # Summary
        # 
        self._Summary.Location = System.Drawing.Point(12, 272)
        self._Summary.Multiline = True
        self._Summary.Name = "Summary"
        self._Summary.Size = System.Drawing.Size(506, 82)
        self._Summary.TabIndex = 7
        self._Summary.Tag = "Summary"
        # 
        # label8
        # 
        self._label8.AutoSize = True
        self._label8.Location = System.Drawing.Point(258, 146)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(48, 13)
        self._label8.Text = "Penciller:"
        # 
        # label9
        # 
        self._label9.AutoSize = True
        self._label9.Location = System.Drawing.Point(12, 175)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(34, 13)
        self._label9.Text = "Inker:"
        # 
        # Inker
        # 
        self._Inker.Location = System.Drawing.Point(57, 171)
        self._Inker.Name = "Inker"
        self._Inker.Size = System.Drawing.Size(139, 20)
        self._Inker.TabIndex = 3
        self._Inker.Tag = "Inker"
        # 
        # Colorist
        # 
        self._Colorist.Location = System.Drawing.Point(312, 171)
        self._Colorist.Name = "Colorist"
        self._Colorist.Size = System.Drawing.Size(139, 20)
        self._Colorist.TabIndex = 4
        self._Colorist.Tag = "Colorist"
        # 
        # label11
        # 
        self._label11.AutoSize = True
        self._label11.Location = System.Drawing.Point(12, 219)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(43, 13)
        self._label11.Text = "Manga:"
        # 
        # Manga
        # 
        self._Manga.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        self._Manga.FormattingEnabled = True
        self._Manga.Items.AddRange(System.Array[System.Object](
            ["",
            "No",
            "Yes",
            "Yes (Right to Left)"]))
        self._Manga.Location = System.Drawing.Point(57, 215)
        self._Manga.Name = "Manga"
        self._Manga.Size = System.Drawing.Size(99, 21)
        self._Manga.TabIndex = 5
        self._Manga.Tag = "Manga"
        # 
        # label10
        # 
        self._label10.AutoSize = True
        self._label10.Location = System.Drawing.Point(180, 219)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(77, 13)
        self._label10.Text = "Black & White:"
        self._label10.UseMnemonic = False
        # 
        # BlackAndWhite
        # 
        self._BlackAndWhite.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        self._BlackAndWhite.FormattingEnabled = True
        self._BlackAndWhite.Items.AddRange(System.Array[System.Object](
            ["",
            "No",
            "Yes"]))
        self._BlackAndWhite.Location = System.Drawing.Point(263, 215)
        self._BlackAndWhite.Name = "BlackAndWhite"
        self._BlackAndWhite.Size = System.Drawing.Size(80, 21)
        self._BlackAndWhite.TabIndex = 6
        self._BlackAndWhite.Tag = "BlackAndWhite"
        # 
        # saveFileDialog
        # 
        self._save_file_dialog.Filter = "ComicRack webcomic|*.cbw"
        # 
        # wpFinished
        # 
        self._wpFinished.Description = "The webcomic file has been created and added into ComicRack"
        self._wpFinished.Controls.Add(self._open_webcomic)
        self._wpFinished.Location = System.Drawing.Point(0, 0)
        self._wpFinished.Name = "wpFinished"
        self._wpFinished.Size = System.Drawing.Size(531, 366)
        self._wpFinished.Style = CristiPotlog.Controls.WizardPageStyle.Finish
        self._wpFinished.TabIndex = 15
        self._wpFinished.Title = "Success"
        #
        # open_webcomic checkbox
        #
        self._open_webcomic.Location = System.Drawing.Point(174, 96)
        self._open_webcomic.Size = System.Drawing.Size(239, 22)
        self._open_webcomic.Text = "Open WebComic in ComicRack"
        self._open_webcomic.TabIndex = 0
        self._open_webcomic.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._open_webcomic.Checked = True
        # 
        # label13
        # 
        self._label13.Location = System.Drawing.Point(13, 172)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(69, 23)
        self._label13.TabIndex = 4
        self._label13.Text = "Image URL:"
        # 
        # label18
        # 
        self._label18.Location = System.Drawing.Point(13, 265)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(116, 23)
        self._label18.TabIndex = 5
        self._label18.Text = "Second Page URL:"
        # 
        # imageUrl
        # 
        self._imageUrl.Location = System.Drawing.Point(111, 169)
        self._imageUrl.Name = "imageUrl"
        self._imageUrl.Size = System.Drawing.Size(408, 20)
        self._imageUrl.TabIndex = 6
        # 
        # linkUrl
        # 
        self._linkUrl.Location = System.Drawing.Point(111, 262)
        self._linkUrl.Name = "linkUrl"
        self._linkUrl.Size = System.Drawing.Size(408, 20)
        self._linkUrl.TabIndex = 7
        # 
        # wpFailedImage
        # 
        self._wpFailedImage.Controls.Add(self._label5)
        self._wpFailedImage.Controls.Add(self._label2)
        self._wpFailedImage.Description = "No available regular expression could match the image on the webcomic page."
        self._wpFailedImage.Location = System.Drawing.Point(0, 0)
        self._wpFailedImage.Name = "wpFailedImage"
        self._wpFailedImage.Size = System.Drawing.Size(531, 366)
        self._wpFailedImage.Style = CristiPotlog.Controls.WizardPageStyle.Finish
        self._wpFailedImage.TabIndex = 16
        self._wpFailedImage.Title = "Failed"
        # 
        # wpFaliedLink
        # 
        self._wpFaliedLink.Controls.Add(self._label14)
        self._wpFaliedLink.Controls.Add(self._label15)
        self._wpFaliedLink.Description = "No available regular expression could match the next page link on the webcomic page."
        self._wpFaliedLink.Location = System.Drawing.Point(0, 0)
        self._wpFaliedLink.Name = "wpFaliedLink"
        self._wpFaliedLink.Size = System.Drawing.Size(531, 366)
        self._wpFaliedLink.Style = CristiPotlog.Controls.WizardPageStyle.Finish
        self._wpFaliedLink.TabIndex = 17
        self._wpFaliedLink.Title = "Failed"
        # 
        # wpProgress
        # 
        self._wpProgress.Controls.Add(self._ProgressText)
        self._wpProgress.Controls.Add(self._ProgressBar)
        self._wpProgress.Location = System.Drawing.Point(0, 0)
        self._wpProgress.Name = "wpProgress"
        self._wpProgress.Size = System.Drawing.Size(531, 366)
        self._wpProgress.TabIndex = 18
        self._wpProgress.Title = "Working"
        # 
        # ProgressBar
        # 
        self._ProgressBar.Location = System.Drawing.Point(12, 172)
        self._ProgressBar.Name = "ProgressBar"
        self._ProgressBar.Size = System.Drawing.Size(507, 23)
        self._ProgressBar.TabIndex = 0
        self._ProgressBar.Maximum = 4
        # 
        # ProgressText
        # 
        self._ProgressText.Location = System.Drawing.Point(13, 202)
        self._ProgressText.Name = "ProgressText"
        self._ProgressText.Size = System.Drawing.Size(506, 44)
        self._ProgressText.TabIndex = 1
        self._ProgressText.Text = "Action"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Transparent
        self._label2.Location = System.Drawing.Point(170, 100)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(344, 33)
        self._label2.TabIndex = 0
        self._label2.Text = "Please notify the script authors by posting the name and url of the webcomic into the forum thread."
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Transparent
        self._label5.Location = System.Drawing.Point(170, 174)
        self._label5.Size = System.Drawing.Size(344, 90)
        self._label5.TabIndex = 1
        self._label5.Text = "Press the restart button to restart with a different webcomic or press Finish to close the script."
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.Transparent
        self._label14.Location = System.Drawing.Point(170, 174)
        self._label14.Size = System.Drawing.Size(344, 90)
        self._label14.TabIndex = 3
        self._label14.Text = "Press the restart button to restart with a different webcomic or press Finish to close the script."
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.Transparent
        self._label15.Location = System.Drawing.Point(170, 100)
        self._label15.Size = System.Drawing.Size(344, 33)
        self._label15.TabIndex = 2
        self._label15.Text = "Please notify the script authors by posting the name and url of the webcomic into the forum thread."
        # 
        # label16
        # 
        self._label16.Location = System.Drawing.Point(13, 114)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(506, 37)
        self._label16.TabIndex = 8
        self._label16.Text = "Enter here the entire url of the very first page of the webcomic. For example:  http://www.giantitp.com/comics/oots0001.html"
        # 
        # label17
        # 
        self._label17.Location = System.Drawing.Point(13, 199)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(506, 36)
        self._label17.TabIndex = 9
        self._label17.Text = "Enter here the entire url of the comic image on the very first page of the webcomic. For example: http://www.giantitp.com/comics/images/oots0001.gif"
        # 
        # label19
        # 
        self._label19.Location = System.Drawing.Point(13, 292)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(506, 51)
        self._label19.TabIndex = 10
        self._label19.Text = "Enter here the  entire url of the second page of the webcomic. For example: http://www.giantitp.com/comics/oots0002.html"
        #
        # background_worker
        #
        self._background_worker.WorkerReportsProgress = True
        self._background_worker.WorkerSupportsCancellation = True
        self._background_worker.DoWork += webcomichelper.webcomic_helper_do_work
        self._background_worker.ProgressChanged += self.worker_progress_changed
        self._background_worker.RunWorkerCompleted += self.worker_completed
        # 
        # wpDisplay
        # 
        self._wpCompositing.Controls.Add(self._border_width)
        self._wpCompositing.Controls.Add(self._right_to_left)
        self._wpCompositing.Controls.Add(self._background_color_label)
        self._wpCompositing.Controls.Add(self._right_to_left_label)
        self._wpCompositing.Controls.Add(self._border_width_label)
        self._wpCompositing.Controls.Add(self._background_color_preview)
        self._wpCompositing.Controls.Add(self._background_color_button)
        self._wpCompositing.Controls.Add(self._width_label)
        self._wpCompositing.Controls.Add(self._height_label)
        self._wpCompositing.Controls.Add(self._rows_label)
        self._wpCompositing.Controls.Add(self._colums_label)
        self._wpCompositing.Controls.Add(self._width)
        self._wpCompositing.Controls.Add(self._height)
        self._wpCompositing.Controls.Add(self._rows)
        self._wpCompositing.Controls.Add(self._columns)
        self._wpCompositing.Controls.Add(self._use_height_and_width)
        self._wpCompositing.Controls.Add(self._use_columns_and_rows)
        self._wpCompositing.Description = "Choose how the webcomic images are displayed"
        self._wpCompositing.Location = System.Drawing.Point(0, 0)
        self._wpCompositing.Name = "wpDisplay"
        self._wpCompositing.Size = System.Drawing.Size(531, 366)
        self._wpCompositing.TabIndex = 0
        self._wpCompositing.Title = "Compositing"
        # 
        # use_columns_and_rows
        # 
        self._use_columns_and_rows.Checked = True
        self._use_columns_and_rows.Location = System.Drawing.Point(12, 78)
        self._use_columns_and_rows.Name = "use_columns_and_rows"
        self._use_columns_and_rows.Size = System.Drawing.Size(175, 24)
        self._use_columns_and_rows.TabIndex = 0
        self._use_columns_and_rows.TabStop = True
        self._use_columns_and_rows.Text = "Use columns and rows"
        self._use_columns_and_rows.UseVisualStyleBackColor = True
        self._use_columns_and_rows.CheckedChanged += self.change_composite_method
        # 
        # use_height_and_width
        # 
        self._use_height_and_width.Location = System.Drawing.Point(12, 144)
        self._use_height_and_width.Name = "use_height_and_width"
        self._use_height_and_width.Size = System.Drawing.Size(300, 24)
        self._use_height_and_width.TabIndex = 5
        self._use_height_and_width.Text = "Use height and width (use only if absolutely required)"
        self._use_height_and_width.UseVisualStyleBackColor = True
        self._use_height_and_width.CheckedChanged += self.change_composite_method
        # 
        # columns
        # 
        self._columns.Location = System.Drawing.Point(115, 108)
        self._columns.Name = "columns"
        self._columns.Size = System.Drawing.Size(38, 20)
        self._columns.TabIndex = 2
        self._columns.Minimum = 1
        # 
        # rows
        # 
        self._rows.Location = System.Drawing.Point(259, 108)
        self._rows.Name = "rows"
        self._rows.Size = System.Drawing.Size(38, 20)
        self._rows.TabIndex = 4
        self._rows.Minimum = 1
        # 
        # height
        # 
        self._height.Location = System.Drawing.Point(143, 174)
        self._height.Maximum = 10000
        self._height.Name = "height"
        self._height.Size = System.Drawing.Size(72, 20)
        self._height.TabIndex = 7
        self._height.Enabled = False
        # 
        # width
        # 
        self._width.Location = System.Drawing.Point(342, 174)
        self._width.Maximum = 10000
        self._width.Name = "width"
        self._width.Size = System.Drawing.Size(72, 20)
        self._width.TabIndex = 9
        self._width.Enabled = False
        # 
        # colums_label
        # 
        self._colums_label.Location = System.Drawing.Point(56, 110)
        self._colums_label.Name = "colums_label"
        self._colums_label.Size = System.Drawing.Size(53, 18)
        self._colums_label.TabIndex = 1
        self._colums_label.Text = "Columns:"
        # 
        # rows_label
        # 
        self._rows_label.Location = System.Drawing.Point(215, 110)
        self._rows_label.Name = "rows_label"
        self._rows_label.Size = System.Drawing.Size(40, 18)
        self._rows_label.TabIndex = 3
        self._rows_label.Text = "Rows:"
        # 
        # height_label
        # 
        self._height_label.Location = System.Drawing.Point(56, 176)
        self._height_label.Name = "height_label"
        self._height_label.Size = System.Drawing.Size(81, 17)
        self._height_label.TabIndex = 6
        self._height_label.Text = "Height (pixels):"
        self._height_label.Enabled = False
        # 
        # width_label
        # 
        self._width_label.Location = System.Drawing.Point(259, 176)
        self._width_label.Name = "width_label"
        self._width_label.Size = System.Drawing.Size(77, 18)
        self._width_label.TabIndex = 8
        self._width_label.Text = "Width (pixels):"
        self._width_label.Enabled = False
        # 
        # background_color_button
        # 
        self._background_color_button.Location = System.Drawing.Point(141, 224)
        self._background_color_button.Name = "background_color_button"
        self._background_color_button.Size = System.Drawing.Size(75, 23)
        self._background_color_button.TabIndex = 12
        self._background_color_button.Text = "Color picker"
        self._background_color_button.UseVisualStyleBackColor = True
        self._background_color_button.Click += self.get_color
        # 
        # background_color_preview
        # 
        self._background_color_preview.BackColor = System.Drawing.Color.White
        self._background_color_preview.Location = System.Drawing.Point(115, 225)
        self._background_color_preview.Name = "background_color_preview"
        self._background_color_preview.Size = System.Drawing.Size(20, 20)
        self._background_color_preview.TabIndex = 11
        self._background_color_preview.BorderStyle = BorderStyle.FixedSingle
        # 
        # border_width_label
        # 
        self._border_width_label.Location = System.Drawing.Point(12, 330)
        self._border_width_label.Name = "border_width_label"
        self._border_width_label.Size = System.Drawing.Size(218, 17)
        self._border_width_label.TabIndex = 15
        self._border_width_label.Text = "Border Width (percentage of page width):"
        # 
        # right_to_left_label
        # 
        self._right_to_left_label.Location = System.Drawing.Point(12, 282)
        self._right_to_left_label.Name = "right_to_left_label"
        self._right_to_left_label.Size = System.Drawing.Size(80, 18)
        self._right_to_left_label.TabIndex = 13
        self._right_to_left_label.Text = "Right to Left:"
        # 
        # background_color_label
        # 
        self._background_color_label.Location = System.Drawing.Point(12, 229)
        self._background_color_label.Name = "background_color_label"
        self._background_color_label.Size = System.Drawing.Size(100, 13)
        self._background_color_label.TabIndex = 10
        self._background_color_label.Text = "Background color:"
        # 
        # right_to_left
        # 
        self._right_to_left.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        self._right_to_left.FormattingEnabled = True
        self._right_to_left.Items.AddRange(System.Array[System.Object](["No","Yes",]))
        self._right_to_left.Location = System.Drawing.Point(89, 279)
        self._right_to_left.Name = "right_to_left"
        self._right_to_left.Size = System.Drawing.Size(50, 21)
        self._right_to_left.TabIndex = 14
        self._right_to_left.SelectedItem = "No"
        # 
        # border_width
        # 
        self._border_width.Location = System.Drawing.Point(216, 328)
        self._border_width.Name = "border_width"
        self._border_width.Size = System.Drawing.Size(39, 20)
        self._border_width.TabIndex = 16
        self._border_width.Maximum = 100
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(531, 414)
        self.Controls.Add(self._wizard)
        self.ShowIcon = False
        self.Text = "Webcomic Helper"
        self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        self.MinimizeBox = False
        self.MaximizeBox = False
        self._wizard.ResumeLayout(False)
        self._wpURL.ResumeLayout(False)
        self._wpURL.PerformLayout()
        self._wpInfo.ResumeLayout(False)
        self._wpInfo.PerformLayout()
        self._wpFailedImage.ResumeLayout(False)
        self._wpFaliedLink.ResumeLayout(False)
        self._wpProgress.ResumeLayout(False)
        self._wpCompositing.ResumeLayout(False)
        self._columns.EndInit()
        self._rows.EndInit()
        self._height.EndInit()
        self._width.EndInit()
        self._border_width.EndInit()
        self.ResumeLayout(False)


    def before_switch_page(self, sender, e):

        #Value checking on the URL page
        if self._wizard.Pages[e.OldIndex] == self._wpURL:
            if self._firstPageUrl.Text.strip() == "":
                MessageBox.Show("First Page URL must be entered")
                e.Cancel = True
                return

            if self._imageUrl.Text.strip() == "":
                MessageBox.Show("Image URL must be entered")
                e.Cancel = True
                return

            if self._linkUrl.Text.strip() == "":
                MessageBox.Show("Second Page URL must be entered")
                e.Cancel = True
                return

        #Handling the back button on the various pages
        if self._wizard.Pages[e.OldIndex] == self._wpFailedImage or self._wizard.Pages[e.OldIndex] == self._wpFaliedLink:
            e.NewIndex = self._wizard.Pages.IndexOf(self._wpURL)
            self._wizard.BackText = "Back"

        if self._wizard.Pages[e.OldIndex] == self._wpInfo and self._wizard.Pages[e.NewIndex] == self._wpProgress:
            e.NewIndex = self._wizard.Pages.IndexOf(self._wpURL)
            return

        #Value checking on the info page
        if self._wizard.Pages[e.OldIndex] == self._wpInfo and self._webcomic_name.Text.strip() == "":
            MessageBox.Show("Webcomic Name cannot be empty")
            e.Cancel = True
            return


        if self._wizard.Pages[e.OldIndex] == self._wpCompositing and self._wizard.Pages[e.NewIndex] == self._wpFinished:
            r = self.save_webcomic()
            if r:
                return
            else:
                e.Cancel = True
                return


    def after_switch_page(self, sender, e):
        
        #URL page to progress page
        if self._wizard.Pages[e.NewIndex] == self._wpProgress:
            self._background_worker.RunWorkerAsync({"FirstPage" : self._firstPageUrl.Text, "Image" : self._imageUrl.Text, "SecondPage" : self._linkUrl.Text, "Form": self})
            
            self._wizard.NextEnabled = False
            self._wizard.BackEnabled = False

        #Change the buttons on the finish page
        if self._wizard.Pages[e.NewIndex] == self._wpFinished:
            self._wizard.NextEnabled = False
            self._wizard.BackEnabled = False
            self._wizard.CancelText = "Finish"


    def wizard_cancel(self, sender, e):
        if self._background_worker.IsBusy or self._background_worker.CancellationPending:
            print "is busy"
            if not self._background_worker.CancellationPending:
                self._background_worker.CancelAsync()
                print "Canceling"

            e.Cancel = True
            return

        print "not busy, exiting"
        self._open_webcomic.Checked = False


    def worker_progress_changed(self, sender, e):
        self._ProgressText.Text = e.UserState
        self._ProgressBar.Value = e.ProgressPercentage


    def worker_completed(self, sender, e):
        #Error
        if e.Error:
            MessageBox.Show(e.Error.Message)
            self._wizard.SelectedPage = self._wpURL

        elif e.Cancelled == True:
            self.Close()
        
        else:
            
            self.result = e.Result

            if self.result._result == WebComicHelperResultEnum.NoImages:
                self._wizard.SelectedPage = self._wpFailedImage
                self._wizard.BackEnabled = True
                self._wizard.NextEnabled = False
                self._wizard.BackText = "Restart"
                self._wizard.CancelText = "Finish"

            elif self.result._result == WebComicHelperResultEnum.NoLinks:
                self._wizard.SelectedPage = self._wpFaliedLink
                self._wizard.BackEnabled = True
                self._wizard.NextEnabled = False
                self._wizard.BackText = "Restart"
                self._wizard.CancelText = "Finish"

            else:
                self._wizard.Next()


    def get_second_image_url(self):
        form = SecondImageUrl()

        r = form.ShowDialog()

        if r == System.Windows.Forms.DialogResult.OK:
            return form._second_image_url.Text

        else:
            return ""


    def get_next_page_link(self):
        form = NextPageLink()

        r = form.ShowDialog()

        if r == System.Windows.Forms.DialogResult.Cancel:
            return NextPageLinkFormResult("", None)

        return form.get_result()


    def get_info(self):
        info = {}

        info["Series"] = self._webcomic_name.Text
        info["Format"] = "Web Comic"

        web = System.Uri(self._firstPageUrl.Text)

        info["Web"] = web.Scheme + "://" + web.Host

        for control in self._info_textboxes:
            if control.Text.strip():
                info[control.Tag] = control.Text

        if self._BlackAndWhite.SelectedItem:
            info["BlackAndWhite"] = self._BlackAndWhite.SelectedItem

        if self._Manga.SelectedItem:
            if self._Manga.SelectedItem == "Yes (Right to Left)":
                info["Manga"] = "YesAndRightToLeft"
            else:
                info["Manga"] = self._Manga.SelectedItem

        return info


    def get_compositing(self):
        
        if self._use_columns_and_rows.Checked:
            return WebComicCompositing(True, self._rows.Value, self._columns.Value, self._background_color_preview.BackColor, self._border_width.Value, self._right_to_left.SelectedItem)

        return WebComicCompositing(False, self._height.Value, self._width.Value, self._background_color_preview.BackColor, self._border_width.Value, self._right_to_left.SelectedItem)



    def save_webcomic(self):
        webcomic = WebComic(self.get_info(), self.get_compositing(), self._firstPageUrl.Text, self.result)
        filepath = self.get_file_location()
        if not filepath:
            MessageBox.Show("A file path is required.", "Empty file path", MessageBoxButtons.OK, MessageBoxIcon.Error)
            return False

        result = webcomic.SaveToXml(filepath)

        if result:
            #Add to ComicRack
            self.book = ComicRack.App.AddNewBook(False)
            self.book.Series = self._webcomic_name.Text
            self.book.Format = "Web Comic"
            self.book.FilePath = filepath
            print "Added " + filepath + " to ComicRack"
            

        return result


    def get_file_location(self):
        self._save_file_dialog.FileName = self._webcomic_name.Text
        result = self._save_file_dialog.ShowDialog()
        if result == DialogResult.OK:
            return self._save_file_dialog.FileName
        else:
            return ""


    def change_composite_method(self, sender, e):
        """Changes which controls are enabled when a compositing radio is checked."""
        self._rows.Enabled = self._use_columns_and_rows.Checked
        self._rows_label.Enabled = self._use_columns_and_rows.Checked
        self._columns.Enabled = self._use_columns_and_rows.Checked
        self._colums_label.Enabled = self._use_columns_and_rows.Checked

        self._height.Enabled = self._use_height_and_width.Checked
        self._height_label.Enabled = self._use_height_and_width.Checked
        self._width.Enabled = self._use_height_and_width.Checked
        self._width_label.Enabled = self._use_height_and_width.Checked


    def get_color(self, sender, e):
        """Shows a color picker dialog and if a new color is chosen, sets the background color of the panel preview to the new color."""
        result = self._color_dialog.ShowDialog()
        if result == DialogResult.OK:
            self._background_color_preview.BackColor = self._color_dialog.Color