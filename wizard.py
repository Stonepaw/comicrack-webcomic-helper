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

from common import WebComicHelperResultEnum, NextPageLinkFormResult, WebComic, HEADER_IMAGE

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
        self._wizard.SuspendLayout()
        self._wpURL.SuspendLayout()
        self._wpInfo.SuspendLayout()
        self._wpFailedImage.SuspendLayout()
        self._wpFaliedLink.SuspendLayout()
        self._wpProgress.SuspendLayout()
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
        self._wizard.Location = System.Drawing.Point(0, 0)
        self._wizard.HeaderImage = Image.FromFile(HEADER_IMAGE)
        self._wizard.Pages.AddRange(System.Array[CristiPotlog.Controls.WizardPage](
            [self._wpURL,
            self._wpProgress,
            self._wpInfo,
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
        self._open_webcomic.Checked = False
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


        if self._wizard.Pages[e.OldIndex] == self._wpInfo and self._wizard.Pages[e.NewIndex] == self._wpFinished:
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
            self._open_webcomic.Checked = True
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


    def save_webcomic(self):
        webcomic = WebComic(self.get_info(), self._firstPageUrl.Text, self.result)
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
