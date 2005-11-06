#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4 on Sat Oct 29 16:44:23 2005

import wx,os.path, locale, wx.html
import Gnumed.pycommon.gmGuiBroker
#_ = lambda x: x

class DermToolDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DermToolDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.population = wx.RadioBox(self, -1, _("Population"), choices=[_("Child"), _("Adult"), _("Elderly")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.distribution = wx.RadioBox(self, -1, _("Distribution"), choices=[_("Truncal"), _("Generalised"), _("Face"), _("Hands"), _("Flexural"), _("Sun-exposed")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.colouring = wx.RadioBox(self, -1, _("Colouring"), choices=[_("None"), _("Pigmented"), _("Depigmented"), _("Erthyema"), _("Purpura")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.pattern = wx.RadioBox(self, -1, _("Pattern"), choices=[_("Confluent"), _("Macular"),  _("Maculo-Papular"), _("Papular"), _("Bullous")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.surface = wx.RadioBox(self, -1, _("Surface"), choices=[_("Flat"), _("Eroded"), _("Crust"), _("Scale"), _("Exudate")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.sensation = wx.RadioBox(self, -1, _("Sensation"), choices=[_("None"), _("Itchy"), _("Painful")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.time_course = wx.RadioBox(self, -1, _("Time Course"), choices=[_("Evolving"), _("Sudden")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.disease_name = wx.TextCtrl(self, -1, "")
        self.disease_list = wx.ListBox(self, -1, choices=[])
        self.image = wx.Panel(self, -1)
        self.image_credit = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.disease_text = wx.html.HtmlWindow(self, -1)
        self.btn_save = wx.Button(self, -1, _("Save"))
        self.btn_close = wx.Button(self, -1, _("Close"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.population)
        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.distribution)
        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.colouring)
        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.pattern)
        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.surface)
        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.sensation)
        self.Bind(wx.EVT_RADIOBOX, self.search_type, self.time_course)
        self.Bind(wx.EVT_TEXT, self.search_text, self.disease_name)
        self.Bind(wx.EVT_LISTBOX, self.open_disease, self.disease_list)
        self.Bind(wx.EVT_BUTTON, self.save, self.btn_save)
        self.Bind(wx.EVT_BUTTON, self.close, self.btn_close)
        # end wxGlade
        self.Bind(wx.EVT_CLOSE, self.close, self)
        self.Bind(wx.EVT_SIZE, self.bind_image, self.image)
        #self.gb = gmGuiBroker.GuiBroker ()
        self.gb= {'resource dir':'/home/ian/gnumed/gnumed/client/'}
        self.diseases = []
        self.path = os.path.join (self.gb['resource dir'], 'data', 'derm')
        for l in file (os.path.join (self.path, 'INDEX')).readlines ():
            row = l.split ()
            d = {}
            lang = locale.getdefaultlocale ()[0][:2]
            n = 0
            for i in ['basename', 'code', 'population', 'distribution', 'colouring', 'pattern', 'surface', 'sensation','time_course']:
                d[i] = row[n]
                n += 1
            txt = file (os.path.join (self.gb['resource dir'], 'data', 'derm', '%s.%s.txt' % (row[0], lang)))
            d['title'] =  txt.readline ()
            d['source'], d['text'] = tuple (txt.read ().split ('\n\n', 1))
            d['text'] = d['text'].replace ('&', '&amp;')
            d['text'] = d['text'].replace ('<', '&lt;')
            d['text'] = d['text'].replace ('>', '&gt;')
            d['text'] = d['text'].replace ('\n\n', '<p>')
            d['source'] = d['source'].split (',')[0]
            self.diseases.append (d)
        

    def __set_properties(self):
        # begin wxGlade: DermToolDialog.__set_properties
        self.SetTitle(_("DermTool"))
        self.population.SetSelection(1)
        self.distribution.SetSelection(0)
        self.colouring.SetSelection(0)
        self.pattern.SetSelection(0)
        self.surface.SetSelection(0)
        self.sensation.SetSelection(0)
        self.time_course.SetSelection(0)
        self.disease_name.SetToolTipString(_("Type name of disease"))
        self.btn_save.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DermToolDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.population, 1, 0, 0)
        sizer_2.Add(self.distribution, 1, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.colouring, 1, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.pattern, 1, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.surface, 1, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.sensation, 1, wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.time_course, 1, wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_4.Add(self.disease_name, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(self.disease_list, 1, wx.ALL|wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.image, 1, wx.EXPAND, 0)
        sizer_5.Add(self.image_credit, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(sizer_5, 3, wx.EXPAND, 0)
        sizer_7.Add(self.disease_text, 1, wx.EXPAND, 0)
        sizer_8.Add(self.btn_save, 0, wx.ADJUST_MINSIZE, 0)
        sizer_8.Add(self.btn_close, 0, wx.ADJUST_MINSIZE, 0)
        sizer_7.Add(sizer_8, 0, wx.EXPAND, 0)
        sizer_6.Add(sizer_7, 2, wx.EXPAND, 0)
        sizer_3.Add(sizer_6, 2, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 2, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def search_type(self, event): # wxGlade: DermToolDialog.<event_handler>
        self.disease_name.Clear ()
        maps = [('population', ['P', 'A', 'E']), ('distribution', ['T', 'G', 'F', 'H', 'L', 'S']), ('colouring', ['N', 'P', 'D', 'E', 'P']), ('pattern', ['C', 'M', 'MP', 'P', 'B']), ('surface', ['F', 'E', 'C', 'S', 'X']), ('sensation', ['N', 'I', 'P']), ('time_course', ['E', 'S'])]
        vals = dict ([(i,j[getattr (self, i).GetSelection ()]) for i, j in maps])
        for i in self.diseases:
            n = 0
            for j in vals:
                if vals[j] == i[j]:
                    n += 1
            i['matches'] = n
        self.diseases.sort (lambda x,y: cmp (x['matches'], y['matches']))
        self.disease_list.Clear ()
        for i in self.diseases[:10]:
            if i['matches'] > 4:
                self.disease_list.Append (i['title'], i)
        

    def open_disease(self, event): # wxGlade: DermToolDialog.<event_handler>
        data = self.disease_list.GetClientData (self.disease_list.GetSelection ())
        self.disease_text.SetPage (data['text'])
        self.image_credit.SetValue (data['source'])
        fname = os.path.join (self.path, data['basename'] + '.jpg')
        if os.path.exists (fname):
            self.jpeg = wx.Image (fname)
            self.bind_image ()
        else:
            print "No image available"

    def bind_image (self, event = None):
        jpg_width = self.jpeg.GetWidth ()
        jpg_height = self.jpeg.GetHeight ()
        pnl_width,pnl_height = self.image.GetSizeTuple ()
        self.image.DestroyChildren ()
        jpg_aspect = jpg_width/float (jpg_height)
        pnl_aspect = pnl_width/float (pnl_height)
        if jpg_aspect > pnl_aspect:
            desired_width = pnl_width
            desired_height = int (pnl_width/jpg_aspect)
            x = 0
            y = (pnl_height-desired_height)/2
        else:
            desired_height = pnl_height
            desired_width = int (pnl_height*jpg_aspect)
            x = (pnl_width-desired_width)/2
            y = 0
        njpeg = self.jpeg.Scale (desired_width, desired_height)
        bmp = wx.BitmapFromImage (njpeg)
        sbmp = wx.StaticBitmap (self.image, -1, bmp, pos=wx.Point (x, y))
        sbmp.Show ()

    def save(self, event): # wxGlade: DermToolDialog.<event_handler>
        print "Event handler `save' not implemented"
        event.Skip()

    def close(self, event): # wxGlade: DermToolDialog.<event_handler>
        self.Destroy ()

    def search_text(self, event): # wxGlade: DermToolDialog.<event_handler>
        self.disease_list.Clear ()
        s = self.disease_name.GetValue ().upper ()
        if len (s) > 3:
            for i in self.diseases:
                if s in i['title'].upper ():
                    self.disease_list.Append (i['title'], i)
                    

# end of class DermToolDialog


    #== if run as standalone =======================================================
if __name__ == '__main__':
	# set up dummy app
	class TestApp (wx.App):
		def OnInit (self):
			frame = DermToolDialog(None, -1)
			frame.Show(True)
			return True
	#---------------------
	wx.InitAllImageHandlers()
	app = TestApp()
	app.MainLoop()
