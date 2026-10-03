# 🏦 Banking Chatbot

A simple **AI-powered banking chatbot** built using **Python, PyTorch, and NLTK**. The chatbot uses a feed-forward neural network to understand user questions and classify them into different banking-related intents.

The chatbot can answer questions related to accounts, cards, payments, money transfers, loans, security, and customer support.

---

## 🚀 Features

* 💬 Interactive chatbot conversation
* 🏦 Banking-related question answering
* 🤖 Intent classification using a neural network
* 🧠 Built with PyTorch
* 🔤 Text processing using NLTK
* 🌱 Stemming and tokenization
* 📊 Bag-of-Words text representation
* 🔐 Banking security-related responses
* 💳 Card-related assistance
* 💸 Money transfer and payment assistance
* 🏦 Account and loan-related queries
* 👋 Greeting and chatbot-information handling
* ❓ Fallback response for low-confidence predictions

---

## 🛠️ Technologies Used

| Technology | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Main programming language                 |
| PyTorch    | Neural network and model training         |
| NLTK       | Text tokenization and stemming            |
| NumPy      | Numerical operations                      |
| JSON       | Storing intents, questions, and responses |

---

## 📂 Project Structure

```text
ChatBotProject/
│
├── intents.json
├── train.py
├── chat.py
├── model.py
├── nltkutils.py
├── data.pth
└── README.md
```

### File Description

#### `intents.json`

Contains the chatbot's training data.

It stores:

* Intent IDs
* Intent tags
* User questions
* Possible chatbot responses

The project currently contains **21 intents**, covering banking operations and general chatbot interaction.

---

#### `nltkutils.py`

Contains the text-processing functions used by the chatbot.

Main functions:

```python
tokenize()
stem()
bag_of_words()
```

### Tokenization

The user's sentence is divided into individual words.

Example:

```text
"How can I check my balance?"
```

becomes approximately:

```text
["How", "can", "I", "check", "my", "balance", "?"]
```

### Stemming

Words are converted to their stem/root form where applicable.

### Bag of Words

The chatbot converts the user's sentence into a numerical vector that can be given to the neural network.

---

#### `model.py`

Contains the feed-forward neural network.

The architecture contains:

```text
Input Layer
     ↓
Linear Layer
     ↓
ReLU
     ↓
Linear Layer
     ↓
ReLU
     ↓
Output Layer
```

The hidden layer size is currently:

```python
hidden_size = 8
```

The output layer contains one class for each intent.

---

#### `train.py`

Responsible for training the chatbot.

The training process is:

```text
intents.json
      ↓
Tokenization
      ↓
Stemming
      ↓
Bag of Words
      ↓
Training Dataset
      ↓
Neural Network
      ↓
Model Training
      ↓
data.pth
```

The trained model is saved in:

```text
data.pth
```

---

#### `chat.py`

Runs the chatbot.

It:

1. Takes the user's input.
2. Tokenizes the sentence.
3. Creates a Bag-of-Words representation.
4. Passes it to the trained neural network.
5. Predicts the intent.
6. Calculates the prediction confidence.
7. Selects a response from the corresponding intent.

Example:

```text
You: hii

Predicted tag: greetings
Confidence: 0.XX

bubbles: Hello! How can I help you?
```

---

## 🧠 How the Chatbot Works

The chatbot follows a simple NLP + machine learning pipeline.

### Step 1 — User Input

The user enters a question:

```text
How can I check my balance?
```

### Step 2 — Tokenization

NLTK separates the sentence into words.

```text
How
can
I
check
my
balance
```

### Step 3 — Stemming

Words are converted into their stemmed forms where applicable.

### Step 4 — Bag of Words

The words are converted into a numerical vector.

For example:

```text
[0, 0, 1, 0, 1, 0, ...]
```

### Step 5 — Neural Network

The vector is passed to the PyTorch neural network.

```text
Input
  ↓
Hidden Layer
  ↓
Hidden Layer
  ↓
Output
```

### Step 6 — Intent Prediction

The network predicts an intent such as:

```text
account_balance
```

### Step 7 — Response

The chatbot selects a response associated with that intent.

```text
bubbles: You can check your balance through online banking or the mobile app.
```

---

## 🏷️ Supported Intents

The chatbot currently supports the following intents:

1. `account_balance`
2. `open_account`
3. `greetings`
4. `lost_card`
5. `card_activation`
6. `forgot_pin`
7. `change_pin`
8. `card_declined`
9. `money_transfer`
10. `transfer_failed`
11. `pending_transaction`
12. `unknown_transaction`
13. `transaction_history`
14. `online_payment_failed`
15. `duplicate_payment`
16. `loan_application`
17. `loan_status`
18. `security`
19. `otp_security`
20. `customer_support`
21. `name`

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd ChatBotProject
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

You should see:

```text
(.venv)
```

in your terminal.

---

### 3. Install Dependencies

Install the required packages:

```bash
pip install torch
pip install nltk
pip install numpy
```

---

## 🏋️ Train the Model

Before running the chatbot, train the neural network:

```bash
python train.py
```

After successful training, you should see:

```text
training complete . file saved to data.pth
```

The trained model is saved as:

```text
data.pth
```

---

## 💬 Run the Chatbot

Start the chatbot using:

```bash
python chat.py
```

You should see:

```text
Let's chat! type 'quit' to exit the chat
```

You can then start chatting.

Example:

```text
You: hii
bubbles: Hello! How can I help you?

You: how can I check my balance
bubbles: You can check your balance through online banking or the mobile app.

You: I lost my card
bubbles: Please block your card immediately through the app or online banking.

You: what is your name
bubbles: My name is CityBank Assistant.
```

To exit:

```text
You: quit
```

---

## 📊 Model Training

The neural network is trained using:

```python
nn.CrossEntropyLoss()
```

and the:

```python
Adam
```

optimizer.

The current training configuration includes:

```python
num_epochs = 300
learning_rate = 0.001
hidden_size = 8
batch_size = 4
```

The trained model is stored in:

```text
data.pth
```

---

## 🔐 Security Intent

The chatbot includes security-related intents such as:

* Account security
* OTP security
* Unauthorized transactions
* Lost or stolen cards

For example:

```text
You: Should I share my OTP?

bubbles: Never share your OTP with anyone.
```

The chatbot is intended as a demonstration project and should not be used to process real banking credentials, OTPs, PINs, or financial information.

---

## ⚠️ Limitations

This project is a beginner-level intent-classification chatbot.

Some limitations include:

* It only understands questions similar to its training data.
* It does not connect to a real banking system.
* It cannot access real account balances.
* It does not perform actual money transfers.
* It does not use a large language model.
* Responses are selected from predefined responses.
* Accuracy depends on the quality and quantity of training examples.

---

## 🔮 Future Improvements

Possible improvements include:

* 🌐 Build a web interface using Django or Flask
* 🤖 Integrate the chatbot into a website
* 🗄️ Add a database
* 🔐 Add user authentication
* 📊 Store and analyze chatbot conversations
* 🧠 Increase the training dataset
* 🎯 Improve intent classification
* 🔊 Add voice input/output
* 📱 Create a responsive chatbot UI
* 🚀 Deploy the chatbot online
* 🔄 Add an API using FastAPI
* 🐳 Dockerize the application
* ⚙️ Add CI/CD for deployment

---

## 🎯 Project Goal

The main goal of this project is to understand how a basic NLP chatbot can be created using:

```text
Natural Language Processing
        +
Bag of Words
        +
Neural Network
        +
Intent Classification
        +
Predefined Responses
```

This project demonstrates the basic workflow of building and training an **intent-based AI chatbot** using Python and PyTorch.

---

## 👩‍💻 Author

**Niyati**

Built as a learning project to explore:

* Python
* NLP
* PyTorch
* Neural Networks
* Chatbot Development
* Machine Learning

