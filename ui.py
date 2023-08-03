from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self,quizq: QuizBrain) -> None:
        self.window = Tk()
        self.window.title("Quiz PY")
        self.quiz = quizq
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

#         self.options = ['Mythology','History','General Knowledge','Science and Nature','Science Gadgets',
# 'Geography',
# 'Computer'
# ]

#         self.clicked = StringVar()
  
# # initial menu text
#         self.clicked.set( 'Mythology' )
#         self.dropmenu = OptionMenu(self.window,self.clicked,
#                                    *self.options)
#         value = self.dropmenu.
#         self.
#         self.dropmenu.grid(row=0,column=0,columnspan=1)

        self.canvas = Canvas(height=250,width=300)
        # self.canvas.config(bg="white")
        self.question = self.canvas.create_text(150,125,text="Some text",width=280,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        # self.rightcanvas = Canvas(height=100,width=100)
        self.rightimage = PhotoImage(file="./images/true.png")
        self.rightbtn = Button(image=self.rightimage,width=100,height=100,highlightthickness=0,command=self.true_check)
        self.rightbtn.grid(row=2,column=0)

        # self.leftcanvas = Canvas(height=100,width=100)
        self.wrongimage = PhotoImage(file="./images/false.png")
        # self.leftcanvas.create_image(100,100,image=self.wrongimage)
        self.wrongbtn = Button(image=self.wrongimage,width=100,height=100,highlightthickness=0,command=self.false_check)
        self.wrongbtn.grid(row=2,column=1)


        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=question_text)
        else:
            self.canvas.itemconfig(self.question,text = "You have reached end of the quiz")
            self.rightbtn.config(state="disabled")
            self.wrongbtn.config(state="disabled")

    
    
    def true_check(self):
        self.give_feedback(self.quiz.check_answer("true"))
        

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def give_feedback(self,isright):
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self
                          .get_next_question)
        

         

        

        
        


        

