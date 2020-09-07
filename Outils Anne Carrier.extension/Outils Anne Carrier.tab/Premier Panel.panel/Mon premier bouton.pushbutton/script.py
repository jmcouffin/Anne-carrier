import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Form,Label,FormStartPosition

TotalCount = 25

def popup(text):
	form = Form()
	form.StartPosition = FormStartPosition.CenterScreen
	form.Width = 300
	form.Height = 300
	form.Text = 'Mais pas tout le temps'	
	label = Label()
	label.Text = text
	label.Width = 300
	label.Height = 300
	label.Parent = form	
	form.ShowDialog()
	
Text = 'Je dis n\'importe quoi'

popup(Text)