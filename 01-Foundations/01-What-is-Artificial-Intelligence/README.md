# What Is Artificial Intelligence?

Artificial Intelligence (AI) is the field of building computer systems that perform tasks normally associated with human intelligence, such as recognizing patterns, making predictions, understanding language, generating content, planning actions, or making decisions.

AI is not one single technology. It is a broad field that includes rule-based systems, machine learning, neural networks, computer vision, speech systems, large language models, and AI agents.

```text
Input                    AI system                    Output
-----                    ---------                    ------
Photo        →     image-recognition model      →     "This is a cat"
Email        →     spam-detection model         →     "Spam"
Question     →     language model               →     written answer
Sales data   →     prediction model             →     future sales estimate
```

## What Makes a System an AI System?

An AI system takes information as input, processes it with rules or a model, and produces an output that supports a decision, prediction, recommendation, or action.

```text
Input → rules or model → output
```

For example, a system can receive weather information, apply decision rules, and recommend an activity. More advanced systems learn the decision rules from examples instead of having a programmer write every rule.

## Main Types of AI

| Type | How it works | Example |
|---|---|---|
| **Rule-based AI** | Uses rules written by people. | “If it is raining, recommend an indoor activity.” |
| **Machine learning** | Learns patterns from examples. | Predicting house prices from previous sales. |
| **Deep learning** | Uses neural networks with many layers. | Image recognition, speech recognition, and translation. |
| **Generative AI** | Creates new text, images, audio, video, or code. | A large language model writing an explanation. |
| **AI agent** | Uses a goal, tools, observations, and decisions to complete tasks. | An assistant that searches a policy and calculates a refund. |

## Supervised and Unsupervised Learning

Machine learning learns patterns from data. Two important approaches are supervised learning and unsupervised learning.

| Approach | Training data | Goal | Example |
|---|---|---|---|
| **Supervised learning** | Input data with correct answers, called labels. | Learn to predict the correct answer for new inputs. | Learn from emails labelled “spam” or “not spam,” then classify a new email. |
| **Unsupervised learning** | Input data without correct-answer labels. | Discover useful groups, patterns, or structure in the data. | Group customers with similar buying behavior. |

```text
Supervised learning
Input: house size + correct price → model learns → predicts a new house price

Unsupervised learning
Input: customer purchase data → model finds patterns → groups similar customers
```

Supervised learning is common when historical examples already have known answers. Unsupervised learning is useful when you want to explore data and do not yet know the right groups or categories.

## AI, Machine Learning, and Deep Learning

These terms are related, but they describe different parts of the field.

```text
Artificial Intelligence
│
├── Rule-based AI
│
└── Machine Learning
    │
    └── Deep Learning
        │
        └── Large Language Models and other generative models
```

- **AI** is the broadest term.
- **Machine learning** is a way to build AI by learning patterns from data.
- **Deep learning** is a type of machine learning based on neural networks.
- **Generative AI** creates new content using a trained model.

## Key Concepts

| Concept | Meaning |
|---|---|
| **Data** | Information used by an AI system, such as text, images, numbers, audio, or records. |
| **Algorithm** | A defined procedure for processing information or solving a problem. |
| **Model** | A learned mathematical representation that makes predictions or generates outputs. |
| **Training** | The process of improving a model using examples. |
| **Inference** | Using a trained model to make a prediction or generate an output. |
| **Feature** | An input value used by a model, such as age, temperature, or a word in a document. |
| **Prediction** | The output estimated by a model. |
| **Evaluation** | Measuring whether the system performs well enough for its intended use. |

## Mathematics Foundations for AI

You do not need to master all mathematics before you begin learning AI. Start with basic Python and AI concepts, then build mathematical understanding as each topic becomes useful.

| Mathematics topic | Why it matters in AI | What to learn first |
|---|---|---|
| **Arithmetic and algebra** | AI uses numbers, formulas, variables, and functions. | Fractions, percentages, equations, graphs, and functions. |
| **Linear algebra** | Data, images, embeddings, and neural-network weights are represented as vectors and matrices. | Vectors, matrices, matrix multiplication, dot products, and dimensions. |
| **Probability** | AI often works with uncertainty and likelihood. | Probability rules, conditional probability, and Bayes’ rule. |
| **Statistics** | Data must be summarized, compared, and evaluated. | Mean, median, variance, distributions, sampling, and correlation. |
| **Calculus** | Training neural networks uses gradients to reduce error. | Derivatives, partial derivatives, and the intuition of gradient descent. |
| **Discrete mathematics and logic** | Useful for algorithms, rule-based systems, and reasoning. | Boolean logic, sets, conditions, and basic algorithmic thinking. |

```text
Data and embeddings      → linear algebra
Uncertainty and metrics  → probability and statistics
Model training           → calculus and optimization
Rules and algorithms     → logic and discrete mathematics
```

For the first Foundations lessons, arithmetic, algebra, and basic statistics are enough. Linear algebra, probability, and calculus become more important when you learn machine learning and neural networks.

## The Basic AI Workflow

Most AI applications follow this general flow:

```text
1. Define a useful problem
2. Collect or provide input data
3. Choose rules or train a model
4. Produce an output
5. Evaluate the result
6. Improve the system over time
```

```text
Customer messages
       │
       ▼
AI classification system
       │
       ▼
"Billing question" / "Technical issue" / "General question"
       │
       ▼
Route the message to the right team
```

## What AI Is Not

AI systems can appear intelligent, but they do not automatically have human understanding, intentions, values, or consciousness.

An AI output can be useful and still be wrong. The system may have incomplete data, an unsuitable model, biased examples, unclear instructions, or a situation it was not designed to handle.

For this reason, good AI systems need testing, monitoring, clear limits, and human oversight when the consequences are important.

## First Runnable Example: Rule-Based AI

The file [rule_based_ai.py](rule_based_ai.py) is a small rule-based AI system. It receives weather information, applies explicit rules, and recommends an activity.

```text
Weather and temperature → decision rules → activity recommendation
```

Run it with Python 3:

```bash
python3 rule_based_ai.py
```

```python
def recommend_activity(is_raining, temperature_celsius):
    if is_raining:
        return "Read a book or visit a museum."
    if temperature_celsius < 10:
        return "Take a short walk and wear a warm coat."
    if temperature_celsius > 28:
        return "Go swimming or find a cool indoor activity."
    return "Go for a walk or have a picnic."
```

This is AI in the classic rule-based sense: the program makes a decision from input using knowledge encoded as rules. It does not learn from data. The next lessons introduce how machine learning learns patterns instead.

## Experiment

Open `rule_based_ai.py` and add a new rule for snowy weather or strong wind. Then run the program again and observe how the output changes.

## Key Takeaways

- AI is a broad field for systems that make predictions, decisions, or generate outputs.
- Some AI systems use rules; others learn from data.
- Machine learning and deep learning are parts of AI.
- AI outputs must be evaluated because they can be incomplete or incorrect.
- A small rule-based program is a useful first step for understanding an AI decision process.

## References

- [Russell and Norvig, *Artificial Intelligence: A Modern Approach*](https://aima.cs.berkeley.edu/) — a comprehensive foundational AI textbook.
- [Alan Turing, *Computing Machinery and Intelligence* (1950)](https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-9) — a seminal paper on machine intelligence.
- [Goodfellow, Bengio, and Courville, *Deep Learning*](https://www.deeplearningbook.org/) — a foundational text for machine learning and neural networks.
