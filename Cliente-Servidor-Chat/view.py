import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class viewClient(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title ="Chat Mosaicode")
        #tamanho da janela
        self.set_default_size(500, 500)
        
        #criacao da grid
        self.grid = Gtk.Grid()
        self.add(self.grid)

        #criacao lista de usuarios
        self.create_user_list()

        #criacao da tela de mensagens
        self.create_text_view()

        #criacao do entry de mensagens
        self.create_entry_text()
    
    def create_text_view(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 1, 0, 4, 10)

        self.textview = Gtk.TextView()
        self.set_border_width(10)
        self.textbuffer = self.textview.get_buffer()
        #self.textbuffer.set_text("---Chat---")
        #self.textview.set_editable()
        #self.textview.set_cursor_visible() 
        scrolledwindow.add(self.textview)

    def create_user_list(self):   
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)    
        self.grid.attach(scrolledwindow, 10, 0, 4, 13)
        self.set_border_width(10)
        self.listbox = Gtk.ListBox()
        
        
    def create_entry_text(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        
        self.grid.attach(scrolledwindow, 1, 10, 4, 1)

        #definindo o entry de mensagens
        self.entry = Gtk.Entry()
        self.entry.set_text("Digite sua mensagem")
        scrolledwindow.add(self.entry)
        
        #definindo o botao enviar
        button_Enviar = Gtk.Button.new_with_label("Enviar")
        self.grid.attach(button_Enviar, 4, 13, 1, 1)
        button_Enviar.connect("clicked", self.on_enviar)

        #definindo o botao negrito
        button_Bold = Gtk.Button.new_with_label("B")
        self.grid.attach(button_Bold, 1, 13, 1, 1)
        button_Bold.connect("clicked", self.tag_bold)

        #definindo o botao italico
        button_Italic = Gtk.Button.new_with_label("I")
        self.grid.attach(button_Italic, 2, 13, 1, 1)
        button_Italic.connect("clicked", self.tag_italic)

        #definindo o botao underline
        button_Underline = Gtk.Button.new_with_label("U")
        self.grid.attach(button_Underline, 3, 13, 1, 1)
        button_Italic.connect("clicked", self.tag_underline)

    def tag_bold (self, button_Bold):
        pass
        #self.textbuffer.create_tag("bold", weight=Pango.Weight.BOLD)

    def tag_italic (self, button_Italic):
        pass
        #button_italic.connect("clicked", self.on_button_clicked, self.tag_italic)
        #self.tag_italic = self.textbuffer.create_tag("italic", style=Pango.Style.ITALIC)
    
    def tag_underline (self, button_Underline):
        pass
        #button_underline.connect("clicked", self.on_button_clicked, self.tag_underline)
        #self.tag_underline = self.textbuffer.create_tag("underline", underline=Pango.Underline.SINGLE)

    #definindo o click do botao
    def on_enviar (self, button_Enviar):
        #pega a mensagem do entry de entrada
        msgn = self.entry.get_text()
        self.textbuffer = self.textview.get_buffer()
        #junta o buffer do textview + nova mensagem
    	self.textbuffer.insert(self.textbuffer.get_end_iter(), "\n"+msgn)


win = viewClient()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()