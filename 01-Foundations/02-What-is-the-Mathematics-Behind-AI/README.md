# What Is the Mathematics Behind AI?

Mathematics is the language AI uses to represent information, describe patterns, handle uncertainty, and improve a model from examples. It does not replace programming or data; it gives models a precise way to work with both.

You do not need to master every subject before starting AI. Learn the ideas gradually, then connect them to real models and code.

```text
Data → mathematical representation → model calculation → prediction or action
```

## The Mathematics Map

| Topic | Main idea | Where it appears in AI |
|---|---|---|
| **Algebra** | Variables, equations, and functions. | A model combines inputs with weights to calculate an output. |
| **Linear algebra** | Vectors, matrices, and transformations. | Images, embeddings, datasets, and neural-network layers. |
| **Probability** | Measuring uncertainty and likelihood. | Confidence scores, language-model next-token choices, and predictions. |
| **Statistics** | Finding patterns and summarizing data. | Understanding a dataset, measuring variation, and evaluating results. |
| **Calculus and optimization** | Measuring change and reducing error. | Training neural networks with gradients and gradient descent. |
| **Logic and discrete mathematics** | Rules, conditions, sets, and algorithms. | Rule-based systems, search, planning, and program design. |

```text
Data and embeddings      → linear algebra
Uncertainty and metrics  → probability and statistics
Learning model weights   → calculus and optimization
Rules and algorithms     → logic and discrete mathematics
```

## 1. Algebra: A Model Is a Function

Algebra lets us describe relationships with variables and functions. A very simple model can be written as:

```text
score = weight × input + bias
```

The **input** is a feature from the data. The **weight** says how strongly that feature affects the score. The **bias** shifts the score up or down.

With more than one feature, a model adds several weighted inputs:

```text
score = w₁x₁ + w₂x₂ + ... + wₙxₙ + bias
```

This simple idea is the starting point for linear regression, logistic regression, and neural networks.

### Example: Estimating a House Price

A simple price-estimation model may use the size of a house as one input:

```text
price estimate = 300 × size in square metres + 50,000
```

For a 100-square-metre house:

```text
price estimate = 300 × 100 + 50,000 = 80,000
```

Here, `300` is the weight: it says how much the estimate changes for each extra square metre. `50,000` is the bias: it shifts the starting estimate. A real model would learn suitable values from historical house sales rather than having us choose them.

## 2. Linear Algebra: How AI Represents Many Numbers

AI rarely works with one number at a time. A group of numbers is a **vector**; a rectangular collection of numbers is a **matrix**.

```text
Feature vector:  [hours studied, practice exams]
Weights vector:  [0.6,            0.3]
```

The **dot product** multiplies matching values and adds them:

```text
[2, 3] · [0.6, 0.3] = (2 × 0.6) + (3 × 0.3) = 2.1
```

In AI, vectors can represent customer attributes, words, sentences, images, or audio. Matrices can represent a whole dataset, a batch of inputs, or the weights in a neural-network layer.

### Example: Features and Weights

Suppose a model uses two features to make a fictional prediction:

```text
Features:  [hours studied, practice exams] = [2, 3]
Weights:   [0.6, 0.3]
```

The dot product combines the values:

```text
(2 × 0.6) + (3 × 0.3) = 2.1
```

The model has given more importance to hours studied (`0.6`) than to completed practice exams (`0.3`). During training, it learns weights that reduce prediction error on its examples.

### Example: An Embedding

An **embedding** is a vector that represents something such as a word, sentence, image, or product. Real embeddings can have hundreds or thousands of dimensions; this small example only illustrates the idea:

```text
"cat"  → [0.8, 0.1, 0.7]
"dog"  → [0.7, 0.2, 0.6]
"car"  → [0.1, 0.9, 0.2]
```

The numbers do not have simple individual meanings. Instead, the position of vectors relative to one another captures patterns learned from data. In this imaginary example, `cat` and `dog` are closer to each other than to `car`, so a model can use their vectors to identify a semantic similarity.

## 3. Probability and Statistics: Working with Uncertainty and Data

Many AI results are uncertain. A classifier may say there is an 82% estimated probability that an email is spam. A language model assigns probabilities to possible next tokens before choosing one.

Probability helps a model express uncertainty. Statistics helps us understand the data that a model learns from.

| Concept | Plain-language meaning | AI example |
|---|---|---|
| **Mean** | The average value. | Average customer spend. |
| **Variance** | How spread out values are. | Whether measurements are consistent or highly variable. |
| **Distribution** | How values are arranged or likely to occur. | The range of model confidence scores. |
| **Conditional probability** | The chance of one event given another. | Probability of spam given the words in an email. |
| **Correlation** | Whether two values tend to change together. | Exploring which features may be useful for prediction. |

Statistics is also essential for evaluating a model: it helps us compare results, detect bias in data, and avoid trusting a result that happened only by chance.

### Example: A Probability Output

An email classifier receives an email containing suspicious links and urgent language. It might calculate:

```text
estimated probability of spam = 0.82 = 82%
```

This does not mean the model knows with certainty that the email is spam. It means that, based on patterns it learned from training data, spam is the more likely outcome. An application can use a threshold to make a decision:

```text
probability ≥ 0.80 → send the email to the spam folder
probability < 0.80 → keep the email in the inbox
```

### Example: Statistics Before Training

Imagine a dataset of customer orders:

```text
Order values: 20, 25, 25, 30, 400
```

The value `400` is much larger than the others. Statistics helps us notice this spread and investigate whether it is a valid large order, a data-entry error, or a case that needs special treatment. Without this step, unusual data can strongly affect a model.

## 4. Calculus and Optimization: How Models Learn

During training, a model makes predictions and compares them with known answers. The difference is measured by a **loss function**.

```text
examples → prediction → loss (error) → adjust weights → better prediction
```

Calculus provides the **gradient**, which tells the model how a small change to each weight changes the loss. **Gradient descent** repeatedly moves the weights in a direction that reduces the loss.

```text
new weight = old weight − learning rate × gradient
```

You do not need to calculate gradients by hand when using modern libraries, but understanding their meaning explains why a neural network can improve through training.

### Example: Reducing Prediction Error

Suppose a model predicts a house price of `90,000`, but the known sale price is `80,000`.

```text
prediction:  90,000
actual:      80,000
error:       10,000
```

The loss function turns that error into a number the model can minimize. The gradient indicates whether each weight should increase or decrease. After many examples, small updates can produce weights that make better predictions overall.

## 5. Logic and Discrete Mathematics: Rules and Algorithms

Logic is the mathematics of true/false conditions and structured reasoning. It is useful for rule-based AI, algorithms, search, planning, and validating program behavior.

```text
IF a payment is overdue AND the account is active
THEN send a payment reminder
```

This is different from machine learning: a person writes the rule instead of the model learning a pattern from data. Many real AI systems combine learned models with ordinary program logic.

### Example: Combining AI and Rules

An AI system may estimate a risk probability, while ordinary logic decides the next action:

```text
AI model: estimated payment-fraud probability = 0.93

IF probability ≥ 0.90
THEN pause the transaction and ask for human review
```

The model supplies a data-driven estimate. The rule makes the business decision clear, testable, and consistent.

## How These Topics Work Together

Consider a simple model that estimates a fictional outcome from two features. The weights below are chosen only for demonstration; a real model would learn them from data.

```text
features                         linear algebra          probability
[hours, practice exams] → weighted sum + bias → score → estimated probability
                                           ↑
                              calculus changes weights during training
```

The model first calculates a score using algebra and linear algebra. It then uses a function called **sigmoid** to convert that score into a number between 0 and 1, which can be read as an estimated probability. The same workflow appears in much larger models, with far more features and parameters.

## A Practical Learning Order

1. **Algebra and functions** — variables, equations, graphs, and percentages.
2. **Vectors and matrices** — dimensions, dot products, and matrix multiplication.
3. **Probability and statistics** — distributions, conditional probability, averages, and variation.
4. **Calculus and optimization** — derivatives, partial derivatives, gradients, and gradient descent.
5. **Logic and algorithms** — Boolean logic, sets, conditions, and computational thinking.

Start with intuition and small examples. Return to the mathematics in more detail when you encounter linear regression, neural networks, embeddings, or model evaluation in later lessons.

## Key Takeaways

- Mathematics lets AI represent data, make calculations, measure uncertainty, and improve models.
- Linear algebra represents features, embeddings, and neural-network weights.
- Probability and statistics help AI reason about uncertainty and data.
- Calculus and optimization explain how models reduce error during training.
- You can begin AI before mastering all of the mathematics, then deepen each topic as it becomes useful.

## References

- [Deisenroth, Faisal, and Ong, *Mathematics for Machine Learning*](https://mml-book.github.io/) — a freely available book covering linear algebra, vector calculus, probability, and optimization for machine learning.
- [Stanford CS229 course materials](https://cs229.stanford.edu/materials.html-full) — freely available review notes for linear algebra, probability theory, and convex optimization.
- [3Blue1Brown linear algebra lessons](https://www.3blue1brown.com/?topic=linear-algebra) — visual explanations of core linear-algebra ideas.
