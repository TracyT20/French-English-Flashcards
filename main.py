from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# Extract text using pandas
words=pandas.read_csv("./data/french_words.csv")
to_learn_dict=words.to_dict("records")
#print(list(to_learn_dict)['French'])
def next_card():
    global current_card,flip_timer,french_word
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn_dict)
    french_word=current_card["French"]
    canvas.itemconfigure(card_title,text="French",fill="Black")
    canvas.itemconfigure(card_image, image=front_image)
    #learn_word=canvas.create_text(400, 263, text=french_word, font=("Arial", 60, "bold"))
    canvas.itemconfigure(learn_word,text=french_word,fill="Black")
    flip_timer=window.after(3000,flip_card)
def flip_card():
    English_word=current_card["English"]
    canvas.itemconfigure(card_image,image=back_image)
    canvas.itemconfigure(card_title,text="English",fill="white")
    canvas.itemconfigure(learn_word,text=English_word,fill="white")

def remove_card():
    try:
        old_words = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        old_words=words
    finally:
        new_df=old_words.drop(old_words[old_words["French"]==french_word].index)
        new_words=new_df.to_csv("./data/words_to_learn.csv",index=False)



#window
window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer=window.after(3000,flip_card)
#canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
front_image=PhotoImage(file="./images/card_front.png")
card_image=canvas.create_image(400, 264, image=front_image)
card_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
back_image = PhotoImage(file="./images/card_back.png")
learn_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
#buttons
wrong_button_image=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=wrong_button_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=3)
right_button_image=PhotoImage(file="./images/right.png")
right_button=Button(image=right_button_image,highlightthickness=0,command=remove_card)
right_button.grid(column=1,row=3)

next_card()




window.mainloop()

