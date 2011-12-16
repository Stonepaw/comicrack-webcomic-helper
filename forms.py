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

clr.AddReference("System.Windows.Forms")

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

from System.Windows.Forms import MessageBox, MessageBoxButtons, DialogResult

from common import NextPageLinkFormResult, ICON

class SecondImageUrl(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._second_image_url = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._okay = System.Windows.Forms.Button()
        self._cancel = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(544, 28)
        self._label1.TabIndex = 0
        self._label1.Text = "The script was unable to match the webcomic image using the built in regular expressions."
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 37)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(544, 30)
        self._label2.TabIndex = 1
        self._label2.Text = "However, the script may be able to build a regular expression to fit this particular webcomic if you enter the entire url of the comic image on the second page."
        # 
        # second_image_url
        # 
        self._second_image_url.Location = System.Drawing.Point(118, 79)
        self._second_image_url.Name = "second_image_url"
        self._second_image_url.Size = System.Drawing.Size(438, 20)
        self._second_image_url.TabIndex = 2
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 82)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 17)
        self._label3.TabIndex = 3
        self._label3.Text = "Second image url:"
        # 
        # okay
        # 
        self._okay.DialogResult = System.Windows.Forms.DialogResult.OK
        self._okay.Location = System.Drawing.Point(400, 112)
        self._okay.Name = "okay"
        self._okay.Size = System.Drawing.Size(75, 23)
        self._okay.TabIndex = 4
        self._okay.Text = "Okay"
        self._okay.UseVisualStyleBackColor = True
        self._okay.Click += self.okay_click
        # 
        # cancel
        # 
        self._cancel.DialogResult = System.Windows.Forms.DialogResult.Cancel
        self._cancel.Location = System.Drawing.Point(481, 112)
        self._cancel.Name = "cancel"
        self._cancel.Size = System.Drawing.Size(75, 23)
        self._cancel.TabIndex = 5
        self._cancel.Text = "Cancel"
        self._cancel.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(12, 102)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(318, 20)
        self._label4.TabIndex = 6
        self._label4.AutoSize = True
        self._label4.Text = "Example: http://www.giantitp.com/comics/images/oots0002.gif"
        # 
        # forms
        # 
        self.ClientSize = System.Drawing.Size(568, 144)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._cancel)
        self.Controls.Add(self._okay)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._second_image_url)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        self.MaximizeBox = False
        self.Icon = System.Drawing.Icon(ICON)
        self.MinimizeBox = False
        self.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent
        self.Text = "Second comic page image url"
        self.AcceptButton = self._okay
        self.CancelButton = self._cancel
        self.ResumeLayout(False)
        self.PerformLayout()


    def okay_click(self, sender, e):
        
        if self._second_image_url.Text.strip() == "":
            self.DialogResult = System.Windows.Forms.DialogResult.None


class NextPageLink(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._image_url = System.Windows.Forms.TextBox()
        self._okay = System.Windows.Forms.Button()
        self._cancel = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._radio_image = System.Windows.Forms.RadioButton()
        self._radio_text = System.Windows.Forms.RadioButton()
        self._link_text = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._help_image = System.Windows.Forms.LinkLabel()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(544, 28)
        self._label1.TabIndex = 0
        self._label1.Text = "The script was unable to match the next page link with the built in regular expressions"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(14, 32)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(544, 30)
        self._label2.TabIndex = 1
        self._label2.Text = "However, the script may be able to build a regular expression to fit this particular webcomic if you enter one of the following options"
        # 
        # image_url
        # 
        self._image_url.Location = System.Drawing.Point(57, 93)
        self._image_url.Name = "image_url"
        self._image_url.Size = System.Drawing.Size(499, 20)
        self._image_url.TabIndex = 2
        # 
        # okay
        # 
        self._okay.DialogResult = System.Windows.Forms.DialogResult.OK
        self._okay.Location = System.Drawing.Point(400, 222)
        self._okay.Name = "okay"
        self._okay.Size = System.Drawing.Size(75, 23)
        self._okay.TabIndex = 4
        self._okay.Text = "Okay"
        self._okay.UseVisualStyleBackColor = True
        self._okay.Click += self.okay_click
        # 
        # cancel
        # 
        self._cancel.DialogResult = System.Windows.Forms.DialogResult.Cancel
        self._cancel.Location = System.Drawing.Point(481, 222)
        self._cancel.Size = System.Drawing.Size(75, 23)
        self._cancel.TabIndex = 5
        self._cancel.Text = "Cancel"
        self._cancel.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(57, 116)
        self._label4.Size = System.Drawing.Size(318, 20)
        self._label4.TabIndex = 6
        self._label4.AutoSize = True
        self._label4.Text = "Example: http://www.giantitp.com/Images/redesign/ComicNav_Next.gif"
        # 
        # radio_image
        # 
        self._radio_image.Location = System.Drawing.Point(13, 68)
        self._radio_image.Size = System.Drawing.Size(249, 25)
        self._radio_image.TabIndex = 8
        self._radio_image.Checked = True
        self._radio_image.TabStop = True
        self._radio_image.Text = "Url of image behind the next page link"
        self._radio_image.UseVisualStyleBackColor = True
        self._radio_image.CheckedChanged += self.check_changed
        # 
        # radio_text
        # 
        self._radio_text.Location = System.Drawing.Point(13, 146)
        self._radio_text.Size = System.Drawing.Size(311, 26)
        self._radio_text.TabIndex = 9
        self._radio_text.TabStop = True
        self._radio_text.Text = "The text on the next page link (only if there is no image)"
        self._radio_text.UseVisualStyleBackColor = True
        # 
        # link_text
        # 
        self._link_text.Location = System.Drawing.Point(57, 178)
        self._link_text.Size = System.Drawing.Size(499, 20)
        self._link_text.TabIndex = 10
        self._link_text.Enabled = False
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(57, 205)
        self._label3.Size = System.Drawing.Size(90, 18)
        self._label3.TabIndex = 11
        self._label3.Text = "Example: next"
        # 
        # help_image
        # 
        self._help_image.AutoSize = True
        self._help_image.Location = System.Drawing.Point(462, 116)
        self._help_image.Name = "help_image"
        self._help_image.Size = System.Drawing.Size(95, 13)
        self._help_image.TabIndex = 12
        self._help_image.TabStop = True
        self._help_image.Tag = """You can usually find this URL by right-clicking on the next page link and choosing "Copy Image URL" or "Copy Image Location"\n\nNote: This will NOT WORK if the image changes when you hover over the image with the mouse since this will copy the url of the hover image."""
        self._help_image.Text = "How do I find this?"
        self._help_image.Click += self.show_help
        # 
        # forms
        # 
        self.AcceptButton = self._okay
        self.CancelButton = self._cancel
        self.ClientSize = System.Drawing.Size(568, 257)
        self.Controls.Add(self._help_image)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._link_text)
        self.Controls.Add(self._radio_text)
        self.Controls.Add(self._radio_image)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._cancel)
        self.Controls.Add(self._okay)
        self.Controls.Add(self._image_url)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        self.MaximizeBox = False
        self.MinimizeBox = False
        self.Icon = System.Drawing.Icon(ICON)
        self.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent
        self.Text = "Next page link"
        self.ResumeLayout(False)
        self.PerformLayout()

    def show_help(self, sender, e):
        MessageBox.Show(sender.Tag, "Help",  MessageBoxButtons.OK, MessageBoxIcon.Information)

    def check_changed(self, sender, e):
        self._image_url.Enabled = self._radio_image.Checked
        self._link_text.Enabled = self._radio_text.Checked

    def okay_click(self, sender, e):
        
        if self._radio_image.Checked == True:
            if self._image_url.Text.strip() == "":
                self.DialogResult = DialogResult.None

        else:
            if self._link_text.Text.strip() == "":
                self.DialogResult = DialogResult.None

    def get_result(self):
        
        if self._radio_image.Checked:
            return NextPageLinkFormResult(self._image_url.Text, True)
        else:
            return NextPageLinkFormResult(self._link_text.Text, False)