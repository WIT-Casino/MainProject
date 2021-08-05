from tkinter import *
from tkinter import ttk
from CasinoBackEnd.playerdata import PlayerData
from CasinoBackEnd.admin import Admin
from CasinoBackEnd.playerdata import PlayerData


class MainApp:
    def __init__(self) -> None:
        pass
        
        #Main App Window
        self.main = Tk()
        self.main.title("Wentworth Casino")
        self.main.configure(bg="red3")

        
        self.admin = Admin()

        self.main_menu()

        self.main.mainloop()

    def player_profile(self, player_info):
        player = PlayerData(player_info[2])
        finances = player.get_finance()
        def profile_frame():
            data_frame = LabelFrame(profile, text="Player Information", font="calibri 12 ",bg="#D3D3D3")
            data_frame.pack(fill="x", expand="yes", padx=20)

            f_label = Label(data_frame, text="First Name", font="calibri 12 ",bg="#D3D3D3")
            f_label.grid(row=0, column=0, padx=10, pady=10)
            f_entry = Entry(data_frame, text=player[0])
            f_entry.grid(row=0, column=1, padx=10, pady=10)

            l_label = Label(data_frame, text="Last Name", font="calibri 12 ",bg="#D3D3D3")
            l_label.grid(row=0, column=2, padx=10, pady=10)
            l_entry = Entry(data_frame, text=player[1])
            l_entry.grid(row=0, column=3, padx=10, pady=10)

            id_label = Label(data_frame, text="ID", font="calibri 12 ",bg="#D3D3D3")
            id_label.grid(row=0, column=4, padx=10, pady=10)
            id_entry = Entry(data_frame, text=player[2])
            id_entry.grid(row=0, column=5, padx=10, pady=10)

            w_label = Label(data_frame, text="Wins", font="calibri 12 ",bg="#D3D3D3")
            w_label.grid(row=1, column=0, padx=10, pady=10)
            w_entry = Entry(data_frame, text=finances[2])
            w_entry.grid(row=1, column=1, padx=10, pady=10)

            ls_label = Label(data_frame, text="Losses", font="calibri 12 ",bg="#D3D3D3")
            ls_label.grid(row=1, column=2, padx=10, pady=10)
            ls_entry = Entry(data_frame, text=finances[3])
            ls_entry.grid(row=1, column=3, padx=10, pady=10)

            b_label = Label(data_frame, text="Balance", font="calibri 12 ",bg="#D3D3D3")
            b_label.grid(row=1, column=4, padx=10, pady=10)
            b_entry = Entry(data_frame, text=finances[1])
            b_entry.grid(row=1, column=5, padx=10, pady=10)

            sk_label = Label(data_frame, text="Skill Rating", font="calibri 12 ",bg="#D3D3D3")
            sk_label.grid(row=2, column=0, padx=10, pady=10)
            sk_entry = Entry(data_frame)
            sk_entry.grid(row=2, column=1, padx=10, pady=10)

            ch_label = Label(data_frame, text="Cheat Rating", font="calibri 12 ",bg="#D3D3D3")
            ch_label.grid(row=2, column=2, padx=10, pady=10)
            ch_entry = Entry(data_frame)
            ch_entry.grid(row=2, column=3, padx=10, pady=10)

            lk_label = Label(data_frame, text="Luck Rating", font="calibri 12 ",bg="#D3D3D3")
            lk_label.grid(row=2, column=4, padx=10, pady=10)
            lk_entry = Entry(data_frame)
            lk_entry.grid(row=2, column=5, padx=10, pady=10)


        def match_table():
            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
            style.map('Treeview', background=[('selected', "blue")])
            list_frame = Frame(profile)
            list_frame.pack(pady=10)
            list_scroll = Scrollbar(list_frame)
            list_scroll.pack(side=RIGHT, fill=Y)
            match_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
            match_list.pack()
            list_scroll.config(command=match_list.yview)
            match_list['columns'] = ("MID", "Won","Lost", "Date")
            match_list.column("#0", width=0, stretch=NO)
            match_list.column("MID", anchor=W, width=100) 
            match_list.column("Won", anchor=CENTER, width=50) 
            match_list.column("Lost", anchor=CENTER, width=50)
            match_list.column("Date", anchor=CENTER, width=50)
            match_list.heading("#0", text="", anchor=W)
            match_list.heading("MID", text="MID", anchor=W)
            match_list.heading("Won", text="Won", anchor='center')
            match_list.heading("Lost", text="Lost", anchor='center')
            match_list.heading("Date", text="Date", anchor='center')

        def graph_frame():
            g_frame = LabelFrame(profile, text="Graphs", font="calibri 12 ",bg="#D3D3D3")
            g_frame.pack(expand="yes", padx=20, side='bottom')

            gid_label = Label(g_frame, text="GID", font="calibri 12 ",bg="#D3D3D3")
            gid_label.grid(row=0, column=0, padx=10, pady=10)
            gid_entry = Entry(g_frame)
            gid_entry.grid(row=0, column=1, padx=10, pady=10)
            mid_label = Label(g_frame, text="MID", font="calibri 12 ",bg="#D3D3D3")
            mid_label.grid(row=1, column=0, padx=10, pady=10)
            mid_entry = Entry(g_frame)
            mid_entry.grid(row=1, column=1, padx=10, pady=10)
            
            n=StringVar()
            mid_graph = ttk.Combobox(g_frame, width = 30, textvariable= n)
            mid_graph['values'] = ('Win/Loss Overtime', 'Win Amount')
            mid_graph.grid(row=0, column=2, padx=10, pady=10)
            mid_graph.current()

            plot = Button(g_frame, text="Plot", width = 10,font="calibri 12 ",bg="#D3D3D3")
            plot.grid(row=1, column=2, padx=10, pady=10)

            
        profile = Tk()
        profile.title("Player Profile")
        profile.configure(bg="#D3D3D3")
        app_width = 800
        app_height = 500
        screen_width = profile.winfo_screenwidth()
        screen_height = profile.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        profile.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        profile_frame()
        match_table()
        graph_frame()


    def player_page(self):
        self.main.withdraw()

        
        def populate_player_table(id = None):
            # Empty table 
            for player in player_list.get_children():
                player_list.delete(player)
            
            records = self.admin.get_all_players_basic_info()
            if id == None:
                for i, record in enumerate(records):
                    player_list.insert(parent='', index='end', iid=i, text="", values=(record[2], record[1], record[0]))
            else:
                new_records = [r for r in records if r[0] == id]
                for i, record in enumerate(new_records):
                    player_list.insert(parent='', index='end', iid=i, text="", values=(record[2], record[1], record[0])) 
        
        def select_record():
            selected = player_list.focus()
            player_info = player_list.item(selected, 'values')

        def go_back():
            self.main.deiconify()
            player.withdraw()

        def player_table():
            style.theme_use('default')
            style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
            style.map('Treeview', background=[('selected', "blue")])
            list_frame.pack(pady=10)
            list_scroll.pack(side=RIGHT, fill=Y)
            player_list.pack()
            list_scroll.config(command=player_list.yview)
            player_list['columns'] = ("First Name", "Last Name","ID")
            player_list.column("#0", width=0, stretch=NO)
            player_list.column("First Name", anchor=W, width=140) 
            player_list.column("Last Name", anchor=W, width=100) 
            player_list.column("ID", anchor=CENTER, width=80)
            player_list.heading("#0", text="", anchor=W)
            player_list.heading("First Name", text="First Name", anchor=W)
            player_list.heading("Last Name", text="Last Name", anchor=W)
            player_list.heading("ID", text="ID", anchor=W)

            populate_player_table()

            return player_list
        
        def search_player_frame():

            data_frame = LabelFrame(player, text="Search Player", font="calibri 12 ", bg="#D3D3D3")
            data_frame.pack(fill="x", expand="yes", padx=20)

            f_label = Label(data_frame, text="First Name", font="calibri 12", bg="#D3D3D3")
            f_label.grid(row=0, column=0, padx=10, pady=10)
            f_entry = Entry(data_frame)
            f_entry.grid(row=0, column=1, padx=10, pady=10)

            l_label = Label(data_frame, text="Last Name",font="calibri 12", bg="#D3D3D3")
            l_label.grid(row=0, column=2, padx=10, pady=10)
            l_entry = Entry(data_frame)
            l_entry.grid(row=0, column=3, padx=10, pady=10)

            id_label = Label(data_frame, text="ID", font="calibri 12", bg="#D3D3D3")
            id_label.grid(row=0, column=4, padx=10, pady=10)
            id_entry = Entry(data_frame)
            id_entry.grid(row=0, column=5, padx=10, pady=10)

            search_btn = Button(data_frame, text="Search", font="calibri 12 ", command= lambda:populate_player_table(id_entry.get()))
            search_btn.grid(row = 0, column=6, padx=10, pady=10)
        
        def cascade_menu(c_menu):

            def add_player():
                
                def addPlayer_function(first, last):
                    addPlayer.destroy()
               
                addPlayer = Toplevel(player)
                addPlayer.title("Add Player")
                addPlayer.configure(bg="#D3D3D3")
                app_width = 450
                app_height = 200
                screen_width = addPlayer.winfo_screenwidth()
                screen_height = addPlayer.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                addPlayer.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                add_frame = LabelFrame(addPlayer, text="Player Information", font="calibri 12 ", bg="#D3D3D3")
                add_frame.pack(padx=10, pady=10)

                first_txt = Label(add_frame, text="First Name", font="calibri 12 ", bg="#D3D3D3")
                first_txt.grid(row=0, column=0, padx=5, pady=5)
                first_entry = Entry(add_frame, font="calibri")
                first_entry.grid(row=1, column=0, padx=5, pady=5)
                crn_txt = Label(add_frame, text="Last Name", font="calibri 12 ", bg="#D3D3D3")
                crn_txt.grid(row=0, column=1, padx=5, pady=5)
                last_entry = Entry(add_frame, font="calibri")
                last_entry.grid(row=1, column=1, padx=5, pady=5)
                

                add_button = Button(addPlayer, text="Add Player", font="calibri 12 ", bg="#D3D3D3", command=lambda:addPlayer_function(first_entry.get(), last_entry.get()))
                add_button.pack(padx=20, pady=20)
              
            def rmv_player():

                def rmvPlayer_function(id):
                    rmvPlayer.destroy()

                rmvPlayer = Toplevel(player)
                rmvPlayer.title("Add Player")
                rmvPlayer.configure(bg="#D3D3D3")
                app_width = 450
                app_height = 200
                screen_width = rmvPlayer.winfo_screenwidth()
                screen_height = rmvPlayer.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2 ) - (app_height / 2)
                rmvPlayer.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

                add_frame = LabelFrame(rmvPlayer, text="Player Information", font="calibri 12 ", bg="#D3D3D3")
                add_frame.pack(padx=10, pady=10)

                id_txt = Label(add_frame, text="ID", font="calibri 12 ", bg="#D3D3D3")
                id_txt.grid(row=0, column=0, padx=5, pady=5)
                id_entry = Entry(add_frame, font="calibri")
                id_entry.grid(row=1, column=0, padx=5, pady=5)

                rmv_button = Button(rmvPlayer, text="Remove Player", font="calibri 12 ", bg="#D3D3D3", command=lambda:rmvPlayer_function(id_entry.get()))
                rmv_button.pack(padx=20, pady=20)

            player.config(menu=c_menu)
            cmd_menu = Menu(c_menu, tearoff=0)
            c_menu.add_cascade(label="Commands", menu=cmd_menu)
            cmd_menu.add_command(label="Add Player", command=add_player)
            cmd_menu.add_command(label="Remove Player", command=rmv_player)

        def command_frame():

            def update_player():
                pass
            
            def reset_List():
                pass
            
            button_frame = LabelFrame(player, text="Commands", font="calibri 12 ",bg="#D3D3D3")
            button_frame.pack(fill="x", expand="yes", padx=20)

            update = Button(button_frame, text="Update Player", font="calibri 12 ",command=update_player)
            update.grid(row=0, column=0, padx=10, pady=10)
            open = Button(button_frame, text="Open Player Profile", font="calibri 12 ",command=self.player_profile(player_info))
            open.grid(row=0, column=1, padx=10, pady=10)
            reset = Button(button_frame, text="Reset List", font="calibri 12 ", command=reset_List)
            reset.grid(row=0, column=2,  padx=10, pady=10 )
        
        player = Tk()
        player.title("Players")
        player.configure(bg="#D3D3D3")
        app_width = 800
        app_height = 500
        screen_width = player.winfo_screenwidth()
        screen_height = player.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        player.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        exit_btn = Button(player, text = 'Exit', font="calibri 12 ", width=7, command = go_back)
        exit_btn.pack(pady=10, side='bottom')
        
        style = ttk.Style()
        list_frame = Frame(player)
        list_scroll = Scrollbar(list_frame)
        player_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
        player_table()
        search_player_frame()
        c_menu = Menu(player)
        cascade_menu(c_menu)
        command_frame()

        player_info = [0]*3 # array with 3 elements
        player_list.bind("<ButtonRelease-1>", select_record)

    def games_page(self):
        self.main.withdraw()

    def revenue_page(self):
        pass
   
    def main_menu(self) -> None:
        app_width = 500
        app_height = 400
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2 ) - (app_height / 2)
        self.main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        lbl1 = Label(self.main, text="CASINO MANAGEMENT SYSTEM", bg="red3", fg="black", font="calibri 24 bold", width=500, anchor=CENTER)
        lbl1.pack()
        player_btn = Button(self.main, text = 'Players', bd = '3', width=10, command=self.player_page)
        game_btn = Button(self.main, text = 'Games', bd = '3', width=10, command=self.games_page)
        rev_btn = Button(self.main, text = 'Revenue', bd = '3', width=10, command=self.revenue_page)
        player_btn.pack(pady=10, ipady=5, side=TOP)
        game_btn.pack(pady=10, ipady=5, side=TOP)
        rev_btn.pack(pady=10, ipady=5, side=TOP)
       
        exit_btn = Button(self.main, text = 'Exit', font="calibri 12 ", width=7, command = self.main.destroy)
        exit_btn.pack(pady=10, side='bottom')
 


GUI = MainApp()