# How Does Machine Learning Learn from Data?

Machine learning learns by finding useful patterns in examples. Instead of a person writing every rule, we give a model data, define what a good answer looks like, measure its mistakes, and adjust the model until it performs well on new examples.

```text
Examples → model makes a prediction → compare with the answer → reduce error → repeat
```

## The Core Idea

Consider a system that identifies spam emails. A programmer could try to write every possible rule:

```text
IF an email says "urgent" AND contains a suspicious link
THEN mark it as spam
```

But spam messages change constantly, and no short list of rules covers every case. A machine-learning model instead learns patterns from many emails already marked as **spam** or **not spam**.

```text
Training examples                 Model learns patterns              New email
-----------------                 --------------------              ---------
"Win a prize now" → spam     →   words, links, sender patterns  →  spam probability
"Meeting at 10"   → not spam
```

The model does not memorize a perfect answer for every email. Its goal is to learn a pattern that generalizes to similar, unseen emails.

## The Learning Cycle

```text
1. Define a problem
2. Collect examples
3. Represent each example as features
4. Train a model on the examples
5. Measure errors
6. Adjust the model
7. Test on unseen data
8. Use, monitor, and improve the model
```

| Step | What happens | Spam-filter example |
|---|---|---|
| **Problem** | Define a useful prediction or decision. | Decide whether an incoming email is spam. |
| **Data** | Gather relevant examples. | Historical emails. |
| **Features** | Turn useful information into a format the model can use. | Link count, sender domain, message length, and word patterns. |
| **Label** | Supply the correct answer for a supervised-learning example. | `spam` or `not spam`. |
| **Training** | Adjust the model using the examples. | Learn which feature patterns often occur in spam. |
| **Prediction** | Apply the learned pattern to a new example. | Estimate whether a new email is spam. |
| **Evaluation** | Check performance on data the model did not train on. | Measure how many spam and legitimate emails are handled correctly. |

## Data: The Source of Learning

Machine learning can only learn from the information it receives. If the examples are incomplete, inaccurate, or unrepresentative, the learned model can also be unreliable.

### Example: House Prices

Imagine historical home-sales records:

| Size (m²) | Bedrooms | Location | Sale price |
|---:|---:|---|---:|
| 70 | 2 | City center | 320,000 |
| 90 | 3 | Suburb | 280,000 |
| 120 | 4 | City center | 510,000 |

Each row is one **example**. The first three columns are possible inputs. The sale price is the correct answer the model tries to predict.

## Features: What the Model Uses as Input

A **feature** is a piece of information that may help a model make a prediction. Good features are relevant, available when the prediction is made, and represented consistently.

For the house-price example:

```text
Raw information: 90 m², 3 bedrooms, suburb

Possible features: [90, 3, location value]
```

Models work with numbers, so text categories such as location must be represented numerically. Later lessons cover data preparation in more detail.

### Example: Useful and Unhelpful Features

For predicting whether a customer will cancel a subscription:

| Feature | Useful? | Why |
|---|---|---|
| Number of support requests | Often useful | It may show frustration or an unresolved problem. |
| Days since last login | Often useful | It may show reduced engagement. |
| Customer ID number | Usually not useful | It is an identifier, not a meaningful behavioral pattern. |
| Cancellation date | Never use as an input | It is only known after the outcome and would leak the answer. |

Using information that is unavailable at prediction time is called **data leakage**. It can make evaluation look excellent while the model fails in real use.

## Labels and Targets: The Answer During Training

In **supervised learning**, each training example includes the answer the model should learn to predict. This answer is called a **label** or **target**.

```text
Features                         Label
[email patterns]             →  spam
[house details]              →  sale price
[image pixels]               →  cat
[customer activity]          →  will cancel
```

There are two common supervised-learning tasks:

| Task | Output | Example |
|---|---|---|
| **Classification** | A category or a probability for a category. | Spam/not spam; cat/dog; approve/reject. |
| **Regression** | A continuous number. | House price; delivery time; energy usage. |

## Training: Learning Weights from Examples

During training, the model starts with adjustable values called **parameters** or **weights**. It uses the input features to make a prediction, compares that prediction with the known label, then updates its weights to reduce future error.

```text
features → model with current weights → prediction
                                      ↓
                               compare with label
                                      ↓
                               calculate loss
                                      ↓
                               update weights
```

### Example: Learning from a Wrong Prediction

A house-price model receives the features for a home and predicts `300,000`. The known sale price is `320,000`.

```text
prediction: 300,000
actual:     320,000
error:       20,000
```

The model uses a **loss function** to turn this difference into a value it can minimize. Training adjusts the weights so that examples with similar features are more likely to receive a better prediction next time.

This does not mean every individual prediction becomes perfect. The model tries to reduce error across many examples, not memorize one row.

## A Worked Example: From Data to Prediction

Suppose we want to predict whether a learner is likely to complete a course. We collect past, fictional examples:

| Weekly study hours | Lessons completed | Completed course? |
|---:|---:|---|
| 1 | 2 | No |
| 2 | 3 | No |
| 5 | 8 | Yes |
| 6 | 10 | Yes |

```text
Features: [weekly study hours, lessons completed]
Label:    completed course? (yes or no)
```

During training, the model may discover that higher study time and more completed lessons are associated with completion in this small dataset. For a new learner with `[5, 7]`, it might produce:

```text
estimated probability of course completion = 0.76 = 76%
```

The 76% is not a guarantee. It is an estimate based on the patterns in the training data. A real model needs many more examples and careful evaluation before it is used for an important decision.

## Training Data, Validation Data, and Test Data

We do not use the same examples for everything. Data is commonly split into separate sets:

```text
Training data   → learns the model weights
Validation data → helps choose settings and improve the model
Test data       → final check on unseen examples
```

### Example: Why the Split Matters

If a student studies only yesterday's quiz questions, they may achieve a perfect score on that quiz but still struggle with new questions. A model can do the same thing: it can memorize training data without learning a general pattern.

Testing on data the model has not seen is how we check whether it can generalize.

## Generalization and Overfitting

**Generalization** means performing well on new, unseen data. This is the goal of machine learning.

**Overfitting** happens when a model learns details or noise from its training data instead of the broader pattern.

```text
Underfitting: model is too simple → poor results on training and new data
Good fit:     learns useful pattern → good results on new data
Overfitting:  memorizes training data → good training result, poor new-data result
```

### Example: Memorizing Instead of Learning

Imagine a model learns that every customer with an ID ending in `7` cancels their subscription because that happened in a small training dataset. That pattern is likely accidental and will probably fail on new customers.

More varied data, simpler models when appropriate, validation, and regularization can help reduce overfitting.

## Learning Without Labels

Not all machine learning requires correct answers in advance.

In **unsupervised learning**, the model receives data without labels and looks for useful structure.

```text
Customer purchase history → find similar patterns → customer groups
```

### Example: Customer Groups

A retailer may use purchase data to discover groups such as:

```text
Group 1: frequent, low-cost purchases
Group 2: occasional, high-value purchases
Group 3: new customers with few purchases
```

The groups were not supplied as labels. The model found them from similarities in the data. A person still needs to decide whether the groups are meaningful and how to use them.

## What Machine Learning Does Not Do Automatically

Machine learning does not automatically understand cause and effect, fairness, business context, or whether a prediction should be acted on.

For example, a model may discover that customers in one area cancel subscriptions more often. That does not explain why, and using location directly may create unfair outcomes. People must examine the data, define appropriate goals, test the model, and set safe decision rules.

## Key Takeaways

- Machine learning learns patterns from examples instead of relying only on hand-written rules.
- Features are inputs; labels are the known answers used in supervised learning.
- Training adjusts weights to reduce loss across many examples.
- Validation and test data help confirm that a model works on unseen data.
- Generalization is the goal; overfitting is memorization that fails on new data.
- Data quality, feature choice, and human judgment are as important as the algorithm.

## References

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — a free interactive introduction covering models, data, generalization, and overfitting.
- [Stanford CS229 course materials](https://cs229.stanford.edu/materials.html-full) — publicly available lecture notes on supervised learning, unsupervised learning, regularization, and model selection.
- [James, Witten, Hastie, Tibshirani, and Taylor, *An Introduction to Statistical Learning*](https://www.statlearning.com/) — freely downloadable introductory books with R and Python editions.
