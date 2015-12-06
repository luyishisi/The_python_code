import wx
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
      wx.Frame.__init__(self, parent, title=title, size=(300, 300))
      self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
                
      self.setupMenuBar()
      self.Show(True)
                          
    def setupMenuBar(self):
      self.CreateStatusBar()
                                  
      menubar = wx.MenuBar()
      menufile = wx.Menu()
                                            
      mnuabout = menufile.Append(wx.ID_ABOUT, '&About', 'about this shit')
      mnuexit = menufile.Append(wx.ID_EXIT, 'E&xit', 'end program')
                                                      
      menubar.Append(menufile, '&File')
                                                            
      self.Bind(wx.EVT_MENU, self.onAbout, mnuabout)
      self.Bind(wx.EVT_MENU, self.onExit, mnuexit)
                                                                              
      self.SetMenuBar(menubar)
                                                                                    
    def onAbout(self, evt):
        dlg = wx.MessageDialog(self, 'This app is a simple text editor', 'About my app', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
                                                                                                                
    def onExit(self, evt):
        self.Close(True)
app = wx.App(False)
frame = MainWindow(None, 'Small Editor')

app.MainLoop()
