from tkinter import *
from tkinter import ttk
from typing import Tuple
from CasinoBackEnd.SQL_Database import SQL_Databases
from CasinoBackEnd.playerdata import PlayerData
from CasinoBackEnd.admin import Admin
from CasinoBackEnd.playerskill import PlayerSkill
from CasinoBackEnd.plotter import Plotter
from CasinoBackEnd.simulation import Simulation


class MainApp:
    def __init__(self) -> None:
        pass
        
        #Main App Window
        self.main = Tk()
        self.main.title("Wentworth Casino")
        self.main.configure(bg="red3")

        self.sql = SQL_Databases()
        self.admin = Admin()
        self.plotter = Plotter()

        self.main_menu()

        self.main.mainloop()

    def player_profile(self, player_info):
        id = player_info[2]
        if id == 0:
            return None
            
        def select_record(event):
                selected = match_list.focus()
                mid_entry.delete(0, END)
                mid_entry.insert(0, match_list.item(selected, 'values')[0])

                gid_entry.delete(0, END)
                gid_entry.insert(0, match_list.item(selected, 'values')[0][0:3])

        def populate_match_table(id = None):
            # Empty table 
            for match in match_list.get_children():
                match_list.delete(match)

            if id == None:
                for i, record in enumerate(records):
                    match_list.insert(parent='', index='end', iid=i, text="", values=(record[1], record[3], record[4], record[2]))
            else:
                new_records = [r for r in records if r[0] == id]
                for i, record in enumerate(new_records):
                    match_list.insert(parent='', index='end', iid=i, text="", values=(record[1], record[3], record[4], record[2])) 
        
        def main_window():
            profile.title("Player Profile")
            profile.configure(bg="#D3D3D3")
            app_width = 1050
            app_height = 500
            screen_width = profile.winfo_screenwidth()
            screen_height = profile.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2 ) - (app_height / 2)
            profile.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        def profile_frame():
            data_frame = LabelFrame(profile, text="Player Information", font="calibri 12 ",bg="#D3D3D3")
            data_frame.pack(fill="x", expand="yes", padx=20)

            f_label = Label(data_frame, text="First Name", font="calibri 12 ",bg="#D3D3D3")
            f_label.grid(row=0, column=0, padx=10, pady=10)
            f_entry = Entry(data_frame)
            f_entry.insert(0,player_info[0])
            f_entry.grid(row=0, column=1, padx=10, pady=10)

            l_label = Label(data_frame, text="Last Name", font="calibri 12 ",bg="#D3D3D3")
            l_label.grid(row=0, column=2, padx=10, pady=10)
            l_entry = Entry(data_frame)
            l_entry.insert(0,player_info[1])
            l_entry.grid(row=0, column=3, padx=10, pady=10)

            id_label = Label(data_frame, text="ID", font="calibri 12 ",bg="#D3D3D3")
            id_label.grid(row=0, column=4, padx=10, pady=10)
            id_entry = Entry(data_frame)
            id_entry.insert(0,player_info[2])
            id_entry.grid(row=0, column=5, padx=10, pady=10)

            w_label = Label(data_frame, text="Amount Won", font="calibri 12 ",bg="#D3D3D3")
            w_label.grid(row=1, column=0, padx=10, pady=10)
            w_entry = Entry(data_frame)
            w_entry.insert(0,finances[1])
            w_entry.grid(row=1, column=1, padx=10, pady=10)

            ls_label = Label(data_frame, text="Amount Lost", font="calibri 12 ",bg="#D3D3D3")
            ls_label.grid(row=1, column=2, padx=10, pady=10)
            ls_entry = Entry(data_frame)
            ls_entry.insert(0,finances[2])
            ls_entry.grid(row=1, column=3, padx=10, pady=10)

            b_label = Label(data_frame, text="Balance", font="calibri 12 ",bg="#D3D3D3")
            b_label.grid(row=1, column=4, padx=10, pady=10)
            b_entry = Entry(data_frame)
            b_entry.insert(0,finances[0])
            b_entry.grid(row=1, column=5, padx=10, pady=10)

            sk_label = Label(data_frame, text="Skill Rating(0-10)", font="calibri 12 ",bg="#D3D3D3")
            sk_label.grid(row=2, column=0, padx=10, pady=10)
            sk_entry = Entry(data_frame)
            sk_entry.insert(0,player_skills.get_skill())
            sk_entry.grid(row=2, column=1, padx=10, pady=10)

            ch_label = Label(data_frame, text="Cheat Rating(0-10)", font="calibri 12 ",bg="#D3D3D3")
            ch_label.grid(row=2, column=2, padx=10, pady=10)
            ch_entry = Entry(data_frame)
            ch_entry.insert(0,player_skills.get_cheat())
            ch_entry.grid(row=2, column=3, padx=10, pady=10)

            lk_label = Label(data_frame, text="Luck Rating(0-10)", font="calibri 12 ",bg="#D3D3D3")
            lk_label.grid(row=2, column=4, padx=10, pady=10)
            lk_entry = Entry(data_frame)
            lk_entry.insert(0,player_skills.get_luck())
            lk_entry.grid(row=2, column=5, padx=10, pady=10)

            populate_match_table()

        def match_table():
            style.theme_use('default')
            style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground ="#D3D3D3")
            style.map('Treeview', background=[('selected', "blue")])
            list_frame.pack(pady=10)
            list_scroll.pack(side=RIGHT, fill='y')
            match_list.pack(padx=10, fill='x', expand='yes')
            list_scroll.config(command=match_list.yview)
            match_list['columns'] = ("MID", "Won","Lost", "Date")
            match_list.column("#0", width=0, stretch=NO)
            match_list.column("MID", anchor=W, width=100) 
            match_list.column("Won", anchor=CENTER, width=100) 
            match_list.column("Lost", anchor=CENTER, width=100)
            match_list.column("Date", anchor=CENTER, width=100)
            match_list.heading("#0", text="", anchor=W)
            match_list.heading("MID", text="MID", anchor=W)
            match_list.heading("Won", text="Won", anchor='center')
            match_list.heading("Lost", text="Lost", anchor='center')
            match_list.heading("Date", text="Date", anchor='center')

        def graph_frame():
            g_frame.pack(expand="yes", padx=20, side='bottom')

            gid_label = Label(g_frame, text="GID", font="calibri 12 ",bg="#D3D3D3")
            gid_label.grid(row=0, column=0, padx=10, pady=10)
            gid_entry.grid(row=0, column=1, padx=10, pady=10)
            mid_label = Label(g_frame, text="MID", font="calibri 12 ",bg="#D3D3D3")
            mid_label.grid(row=1, column=0, padx=10, pady=10)
            mid_entry.grid(row=1, column=1, padx=10, pady=10)
            
            mid_graph['values'] = ('Win/Loss Overtime', 'Won Amount', 'Lost Amount')
            mid_graph.grid(row=0, column=2, padx=10, pady=10)
            mid_graph.current()

            plot = Button(g_frame, text="Plot", width = 10,font="calibri 12 ",bg="#D3D3D3", command=lambda: show_graph(mid_graph.get()))
            plot.grid(row=1, column=2, padx=10, pady=10)

            simul = Button(g_frame, text="Simulation", font="calibri 12", command=lambda: show_simulation(100))
            simul.grid(row=1, column=3,  padx=10, pady=10)

        def show_graph(graph_type):
            if graph_type == "Win/Loss Overtime":                
                amount_won = [record[3] for record in records]
                amount_lost = [record[4] for record in records]
                date = [record[2] for record in records]
                self.plotter.twoLinePlot(date, amount_won, date, amount_lost, "Date", "Amount", "Amount Won/Losses over Time", True)
            elif graph_type == "Won Amount":
                amount_won = [0]*8
                for record in records:
                    i = int(record[1][0:3]) - 1
                    amount_won[i] = amount_won[i] + record[3]
                labels = ["Black Jack", "Craps", "Roullete", "Slots", "Keno","Poker","Baccarat","Big Six"]
                self.plotter.pieChart(amount_won, labels, "Amount Won in Each Game", explode=True)
            elif graph_type == "Lost Amount":
                amount_lost = [0]*8
                for record in records:
                    i = int(record[1][0:3]) - 1
                    amount_lost[i] = amount_lost[i] + record[4]
                labels = ["Black Jack", "Craps", "Roullete", "Slots", "Keno","Poker","Baccarat","Big Six"]
                self.plotter.pieChart(amount_lost, labels, "Amount Lost in Each Game", explode=True)
             
            else:
                pass

        def show_simulation(num_games):
            # nonlocal player_skills
            simul = Simulation()
            player_skill_data = []
            player_skill_data.append(player_skills.get_skill())
            player_skill_data.append(player_skills.get_luck())
            player_skill_data.append(player_skills.get_cheat())

            simul.simOnePlayerNGames(player_skill_data, 0.25, num_games)


        player = PlayerData(id)
        finances = player.get_finance()
        records = player.get_all_matches()
        records = sorted(records, key=lambda x: x[2]) # sorted by date
        player_skills = PlayerSkill(id)

        ### Create widgets
        # Profile frame
        profile = Tk()

        # Match table
        style = ttk.Style()
        list_frame = Frame(profile)
        list_scroll = Scrollbar(list_frame)
        match_list = ttk.Treeview(list_frame, yscrollcommand=list_scroll.set, selectmode="extended")
        
        match_list.bind("<ButtonRelease-1>", select_record)

        # Graph Frame
        g_frame = LabelFrame(profile, text="Graphs", font="calibri 12 ",bg="#D3D3D3")
        gid_entry = Entry(g_frame)
        mid_entry = Entry(g_frame)
        n=StringVar()
        mid_graph = ttk.Combobox(g_frame, width = 30, textvariable= n)

        # Configure widgets
        main_window()
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
            open = Button(button_frame, text="Open Player Profile", font="calibri 12 ",command=lambda: self.player_profile(player_info))
            open.grid(row=0, column=1, padx=10, pady=10)
            reset = Button(button_frame, text="Reset List", font="calibri 12 ", command=reset_List)
            reset.grid(row=0, column=2,  padx=10, pady=10 )
            
        
        def select_record(event):
            nonlocal player_info
            selected = player_list.focus()
            player_info = player_list.item(selected, 'values')

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
        player_info = [0]*3 # array with 3 elements
        player_list.bind("<ButtonRelease-1>", select_record)
        command_frame()

        
    def games_page(self):
        pass
            

    def revenue_page(self):
        match_data = self.sql.select_from("MatchData", "*")
        records_by_date = sorted(match_data, key=lambda x: x[2])

        profit = []
        date = []
        day_profit = 0        

        for i, record in enumerate(records_by_date, start=0):
            day_profit = day_profit + record[3] - record[4]
            current_day = record[2]
            if i == len(records_by_date)-1:
                next_day = current_day
            else:
                next_day = records_by_date[i+1][2]

            if current_day != next_day:
                profit.append(day_profit)
                date.append(current_day)
                day_profit = 0
            
        self.plotter.linePlot(date, profit, "Date", "Profit", "Profit for Each Day", 1)

        game_data = self.sql.select_from("GameMain", "*")
        labels = [record[1] for record in game_data]
        won = [record[2] for record in game_data]   # Player won here so casino lost
        lost = [record[3] for record in game_data]  # and vice versa
        self.plotter.pieChart(lost, labels, "Amount Earned in Each Game", explode=True)
        self.plotter.pieChart(won, labels, "Amount Lost in Each Game", explode=True)

   
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