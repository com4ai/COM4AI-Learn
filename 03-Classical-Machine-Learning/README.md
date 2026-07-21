# Classical Machine Learning

Classical machine learning is a group of algorithms that learn a relationship between data and an outcome. A person or system prepares useful input values—called **features**—then a learning algorithm finds patterns that can be used to make a prediction, classification, or grouping.

It is widely used for structured data: rows and columns from spreadsheets, databases, sensors, transactions, forms, and business systems.

```text
Historical data → features → learning algorithm → trained model → prediction or decision
```

## The Main Idea

Suppose a company wants to predict whether a customer will cancel a subscription. Its historical data may contain one row per customer:

| Months subscribed | Support requests | Monthly cost | Cancelled? |
|---:|---:|---:|---|
| 2 | 5 | 20 | Yes |
| 24 | 0 | 20 | No |
| 8 | 2 | 35 | No |

The first three columns are features. `Cancelled?` is the **target**: the answer the model should learn to predict. During training, the algorithm looks for patterns in examples where the answer is already known. For a new customer, it estimates whether cancellation is likely.

## A Classical ML Workflow

```text
Define the problem
        ↓
Collect and prepare data
        ↓
Choose features and a model
        ↓
Train with historical examples
        ↓
Evaluate on unseen data
        ↓
Use, monitor, and improve the model
```

The quality of the data and features is often as important as the algorithm. A model cannot learn a reliable signal if its examples are incomplete, biased, incorrectly labelled, or unrelated to the question being asked.

## Common Types of Classical Machine Learning

| Type | What the data contains | Typical result | Example |
|---|---|---|---|
| Supervised learning | Inputs and known answers | A prediction or label | Predict delivery time; classify an email as spam or not spam. |
| Unsupervised learning | Inputs without known answers | Groups or structure | Group customers with similar buying patterns. |
| Regression | A numeric target | A number | Estimate house price or energy demand. |
| Classification | A category target | A class or probability | Detect fraud or identify a product category. |

Regression and classification are common forms of supervised learning. Clustering is a common form of unsupervised learning.

## Common Algorithms

- **Linear regression** estimates a numeric value from input features.
- **Logistic regression** estimates the probability of a class, such as fraud or not fraud.
- **Decision trees** learn a sequence of understandable if/then choices.
- **Random forests** combine many decision trees to produce a more stable result.
- **Support vector machines (SVMs)** find a boundary that separates classes.
- **k-nearest neighbors (k-NN)** predicts based on similar examples in the data.
- **k-means** groups similar examples into clusters when no labels are available.

No algorithm is automatically best. The appropriate model depends on the problem, amount and type of data, accuracy requirement, explanation needs, latency, and cost.

## Where It Is Used

- Fraud and anomaly detection for financial transactions.
- Demand, sales, price, and energy forecasting.
- Spam filtering and document classification.
- Customer churn prediction and recommendation features.
- Quality prediction and predictive maintenance in manufacturing.
- Risk scoring and operational decision support.

## Limitations

Classical ML does not understand the world in the way people do. It learns statistical patterns from the examples it receives. A model can fail when the real world changes, when new data differs from the training data, or when important information is missing from the features. Evaluation, monitoring, and responsible use are therefore part of every ML system.

## References

- [An Introduction to Statistical Learning](https://www.statlearning.com/) — free textbook on core statistical learning methods.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — practical documentation for classical ML algorithms and workflows.
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — introductory lessons and exercises.
- [The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/) — advanced reference on statistical learning methods.
