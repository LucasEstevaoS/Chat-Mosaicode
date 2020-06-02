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

        #criacao do toolbar para edicao das mensagens
        self.create_toolbar()

    #parte que vai aparecer as mensagens (alimentada pelo servidor)    
    def create_text_view(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 1, 0, 4, 10)
        self.textview = Gtk.TextView()

        #tenho que deixar o textview nao editavel e desabilitar cursor
        #self.textview.set_editable()
        #self.textview.set_cursor_visible()
        
        self.set_border_width(10)
        self.textbuffer = self.textview.get_buffer()
         
        scrolledwindow.add(self.textview)

    #parte onde ira aparecer uma lista com os usuarios
    def create_user_list(self):   
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)    
        self.grid.attach(scrolledwindow, 10, 0, 4, 13)
        self.set_border_width(10)
        self.listbox = Gtk.ListBox()
        
    #parte da entrada de texto do chat (alimentado pelo usuario)    
    def create_entry_text(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        
        self.grid.attach(scrolledwindow, 1, 10, 4, 1)

        #definindo o entry de mensagens
        self.entry = Gtk.Entry()
        scrolledwindow.add(self.entry)
        
        #definindo o botao enviar
        button_Enviar = Gtk.Button.new_with_label("Enviar")
        self.grid.attach(button_Enviar, 4, 13, 1, 1)
        button_Enviar.connect("clicked", self.on_enviar)

       
    # toolbar que contem negrito, italico e sublinhado
    def create_toolbar(self):
        self.toolbar = Gtk.Toolbar()
        self.grid.attach(self.toolbar, 1, 13, 1, 1)

        button_bold = Gtk.ToolButton()
        button_bold.set_icon_name("format-text-bold-symbolic")
        self.toolbar.insert(button_bold, 0)

        button_italic = Gtk.ToolButton()
        button_italic.set_icon_name("format-text-italic-symbolic")
        self.toolbar.insert(button_italic, 1)

        button_underline = Gtk.ToolButton()
        button_underline.set_icon_name("format-text-underline-symbolic")
        self.toolbar.insert(button_underline, 2)

        #button_bold.connect("clicked", self.on_button_clicked, self.tag_bold)
        #button_italic.connect("clicked", self.on_button_clicked, self.tag_italic)
        #button_underline.connect("clicked", self.on_button_clicked, self.tag_underline)

        self.toolbar.insert(Gtk.SeparatorToolItem(), 3)


    def on_button_clicked(self, widget, tag):
        pass
        '''bounds = self.textbuffer.get_selection_bounds()
        if len(bounds) != 0:
            start, end = bounds
            self.textbuffer.apply_tag(tag, start, end)
        '''

    #definindo o click do botao enviar
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