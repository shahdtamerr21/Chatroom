import socket
import threading
import tkinter as tk

# Function to handle receiving messages from the server
def receive():
    while True:
        try:
            # Receive message from server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # Update chat display with received message
                chat_display.insert(tk.END, message + '\n')
        except:
            # Close connection on error
            print("An error occurred!")
            client.close()
            break

# Function to handle sending messages to the server
def send(event=None):
    message = '{}: {}'.format(nickname, input_field.get())
    input_field.delete(0, tk.END)
    client.send(message.encode('ascii'))

# Choosing Nickname
nickname = input("Choose your name: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Create main window
root = tk.Tk()
root.title("Chat")

# Create chat display
chat_display = tk.Text(root, height=20, width=50)
chat_display.pack()

# Create input field
input_field = tk.Entry(root, width=50)
input_field.pack(side=tk.BOTTOM, fill=tk.X)

# Bind the Enter key to send messages
input_field.bind("<Return>", send)

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=send)
send_button.pack(side=tk.BOTTOM)

# Start thread for receiving messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start GUI main loop
root.mainloop()
