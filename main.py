import backend_code as bc
from tkinter import Button, Label, Frame, END, Text, Tk, WORD 



class Application(Frame):
    def __init__(self, master):
        """This initializes the frame"""
        super(Application, self).__init__(master)
        self.timer = 0
        self.paused = False
        self.pause_time = 0
        self.grid()
        self.create_widgets()
        self.reset_timer()


    @property
    def clockformat(self):
      return bc.clock_format(self.timer)


    @property
    def pauseformat(self):
      return bc.clock_format(self.pause_time)
       

    def create_widgets(self):
        self.countdown_lbl = Label(self, text = "Countdown timer")
        self.countdown_lbl.grid(row = 0, column = 0, columnspan=2)

        self.add_1_min = Button(self, text = "1 Min", command = self.add_1_minute_to_timer)
        self.add_1_min.grid(row = 1, column = 0, sticky = 'W')

        self.add_10_sec = Button(self, text = '10 sec', command = self.add_10_seconds_to_timer)
        self.add_10_sec.grid(row = 1, column = 1, sticky = 'E')

        self.add_1_sec = Button(self, text = '1 sec', command = self.add_1_seconds_to_timer)
        self.add_1_sec.grid(row = 2, column = 0, sticky = 'W')

        self.start = Button(self, text = 'Start', command = self.start_timer)
        self.start.grid(row = 2, column = 1, sticky = 'E')

        self.stop = Button(self, text = 'Stop', command = self.stop_timer)
        self.stop.grid(row = 3, column = 0, sticky = 'W')

        self.reset = Button(self, text = 'Reset', command = self.reset_timer)
        self.reset.grid(row = 3, column = 1, sticky = 'E')

        self.text_box = Text(self, width = 20, height = 2, wrap = WORD)
        self.text_box.grid(row = 6, column = 0, columnspan=2, sticky = 'W')


    def add_1_minute_to_timer(self):
      self.timer += 60 
      self.text_box.delete(0.0, END)
      self.text_box.insert(0.0, self.clockformat)

  
    def add_10_seconds_to_timer(self):
      self.timer += 10
      self.text_box.delete(0.0, END)
      self.text_box.insert(0.0, self.clockformat)
      
      
    def add_1_seconds_to_timer(self):
      self.timer += 1
      self.text_box.delete(0.0, END)
      self.text_box.insert(0.0, self.clockformat)


    def start_timer(self):
      if self.timer >= 0 and self.paused == False:
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, self.clockformat)
        self.timer -= 1
        self.after(1000, self.start_timer) 
      elif self.paused:
        self.paused = False
        self.timer = self.pause_time


    def stop_timer(self):
      self.paused = True
      self.pause_time = self.timer
      self.text_box.delete(0.0, END)
      self.text_box.insert(0.0, self.pauseformat)
      self.timer = 0
      
      
    def reset_timer(self):
      self.timer = 0
      self.text_box.delete(0.0, END)
      self.text_box.insert(0.0, '00:00')


root = Tk()
root.title("Stopwatch")
root.resizable(height = None, width = None)
root.geometry("180x160")
root = Application(root)
root.mainloop()