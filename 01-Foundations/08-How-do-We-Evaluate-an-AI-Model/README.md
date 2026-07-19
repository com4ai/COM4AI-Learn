# How Do We Evaluate an AI Model?

Evaluating an AI model means checking whether it is accurate, useful, reliable, and safe enough for its intended task. A model is not good simply because it produces an answer or scores well on training data. It must be measured on relevant examples it did not learn from, using metrics that match the cost of mistakes.

```text
Define success → evaluate on unseen data → inspect errors → improve → monitor in real use
```

## Start with the Real Decision

Before choosing a metric, define what the model is meant to do and what happens when it makes different kinds of mistakes.

### Example: Spam Filtering

For a spam filter, there are two important mistakes:

```text
False positive: a legitimate email is sent to spam
False negative: a spam email remains in the inbox
```

Both are bad, but a business may consider a missed customer email more costly than a spam message left in the inbox. That choice should guide the evaluation.

| Question | Example answer |
|---|---|
| What is the model’s task? | Classify an incoming email as spam or not spam. |
| Who is affected? | Email users and support staff. |
| What happens if it is wrong? | A user may miss an important message or see unwanted spam. |
| What level of performance is needed? | Depends on volume, user expectations, and the cost of each error. |
| When should a human review the result? | When the model is uncertain or the consequences are important. |

## Use Data the Model Has Not Seen

Training data teaches the model. Evaluation data tests whether it can generalize to new examples.

```text
Training set   → learn weights and patterns
Validation set → compare choices and tune settings
Test set       → final evaluation on unseen data
```

The test set should resemble the data the model will face in real use. If a spam model is tested only on old, simple spam messages, a high score may not predict performance against new attack patterns.

### Example: Testing on New Emails

```text
Training: historical emails from January to October
Validation: emails from November
Test: emails from December
```

For problems that change over time, this time-based split is often more realistic than mixing all months randomly.

## Classification Evaluation: The Confusion Matrix

For a two-class problem such as spam/not spam, every prediction belongs to one of four outcomes:

|  | Actually spam | Actually not spam |
|---|---:|---:|
| **Predicted spam** | True positive (TP) | False positive (FP) |
| **Predicted not spam** | False negative (FN) | True negative (TN) |

### Example: Spam Filter Results

Suppose the test set contains 100 emails:

|  | Actually spam | Actually not spam |
|---|---:|---:|
| **Predicted spam** | 30 | 5 |
| **Predicted not spam** | 10 | 55 |

```text
TP = 30: spam correctly caught
FP = 5: legitimate emails incorrectly sent to spam
FN = 10: spam emails missed
TN = 55: legitimate emails correctly kept in the inbox
```

The table tells a more useful story than one overall score because it shows the kinds of errors the model makes.

## Core Classification Metrics

| Metric | Question it answers | Formula | When it is useful |
|---|---|---|---|
| **Accuracy** | How often was the prediction correct? | `(TP + TN) / all examples` | A rough measure when classes are balanced and error costs are similar. |
| **Precision** | When the model says “positive,” how often is it right? | `TP / (TP + FP)` | When false positives are costly. |
| **Recall** | Of all real positive cases, how many did the model find? | `TP / (TP + FN)` | When missing a positive case is costly. |
| **F1 score** | How well does the model balance precision and recall? | Harmonic mean of precision and recall. | When both kinds of error matter, especially with imbalanced classes. |
| **False-positive rate** | How often are negative cases wrongly flagged? | `FP / (FP + TN)` | When false alarms are important. |

### Example: Calculate Metrics from the Spam Filter

Using `TP = 30`, `FP = 5`, `FN = 10`, and `TN = 55`:

```text
Accuracy  = (30 + 55) / 100 = 85%
Precision = 30 / (30 + 5)  = 85.7%
Recall    = 30 / (30 + 10) = 75%
F1 score  = about 80%
```

The model is correct overall 85% of the time, but it misses 25% of spam emails. Whether that is acceptable depends on the purpose and the costs of missed spam versus wrongly blocked legitimate mail.

## Why Accuracy Alone Can Be Misleading

Imagine a disease-detection task where only 1 out of 100 people has the disease. A model that always predicts “no disease” is 99% accurate, but it detects no cases at all.

```text
Accuracy: 99%
Recall for disease cases: 0%
```

For rare or high-risk events, recall, precision, false-positive rate, and careful review are usually more meaningful than accuracy alone.

## Thresholds: Turning a Score into a Decision

Many classification models produce a probability or score. An application chooses a **threshold** to turn the score into a label.

### Example: Spam Threshold

```text
spam probability ≥ 0.80 → send to spam
spam probability < 0.80 → keep in inbox
```

Changing the threshold changes the tradeoff:

| Threshold choice | Likely effect |
|---|---|
| Lower threshold | Catches more spam (higher recall), but may block more legitimate email (lower precision). |
| Higher threshold | Blocks fewer legitimate emails (higher precision), but may miss more spam (lower recall). |

The right threshold is a product decision, not a universal number.

## ROC Curves and AUC: Comparing Thresholds

A **ROC curve** (Receiver Operating Characteristic curve) shows how a classifier behaves across many possible thresholds. It plots:

```text
x-axis: false-positive rate
y-axis: true-positive rate (recall)
```

Each point on the curve represents a different threshold. Moving to a lower threshold usually catches more real positive cases, but it also creates more false positives.

### Example: Spam Classifier Thresholds

| Spam threshold | Recall: spam caught | False-positive rate: legitimate email wrongly blocked |
|---:|---:|---:|
| 0.90 | 55% | 1% |
| 0.70 | 75% | 4% |
| 0.50 | 90% | 13% |

```text
Lower threshold → higher recall, but more false alarms
Higher threshold → fewer false alarms, but more missed positives
```

The **AUC** (Area Under the ROC Curve) summarizes the ROC curve with one value:

| AUC value | General interpretation |
|---:|---|
| 1.0 | Perfect separation of positive and negative cases. |
| 0.5 | No better than random ranking. |
| Below 0.5 | The ranking is worse than random; investigate the model or label direction. |

AUC is useful for comparing how well models rank positive examples above negative ones across thresholds. It does **not** choose the right operating threshold for a real application. You still need to consider the cost of false positives and false negatives.

For highly imbalanced problems, a **precision–recall curve** is often also important because it focuses on the quality of positive predictions and on finding actual positive cases.

## Micro, Macro, and Weighted Averages for Multiple Classes

When a model predicts more than two classes, such as `cat`, `dog`, and `bird`, precision, recall, and F1 can be calculated for each class separately. An average then gives one summary value.

| Average | How it is calculated | When it is useful |
|---|---|---|
| **Micro average** | Add all true positives, false positives, and false negatives across classes first, then calculate one metric. | Shows overall performance across individual predictions; common when each prediction has equal importance. |
| **Macro average** | Calculate the metric for each class, then take the simple average. | Gives every class equal importance, including rare classes. |
| **Weighted average** | Calculate the metric for each class, then average using the number of real examples in each class as a weight. | Summarizes overall performance while accounting for class frequency. |

### Example: Three Animal Classes

```text
Test data:
cat:  900 images
dog:   90 images
bird:  10 images
```

If a model performs well on cats but poorly on birds:

```text
Micro average:   may look high because cats are most examples
Weighted average: also strongly reflects cat performance
Macro average:   falls because birds count equally with cats and dogs
```

Use per-class metrics and the confusion matrix alongside any average. A single micro or weighted score can hide a poor result for a rare but important class.

## Regression Evaluation: Predicting a Number

**Regression** models predict a numerical value, such as a house price, delivery time, or energy use. Their errors are measured as the distance between predicted and actual values.

| Metric | Meaning | Example use |
|---|---|---|
| **MAE: Mean Absolute Error** | Average size of the errors. | Average price-estimation error. |
| **MSE: Mean Squared Error** | Squares errors, penalizing large mistakes more heavily. | When large errors are especially costly. |
| **RMSE: Root Mean Squared Error** | Square root of MSE, expressed in the target’s original unit. | Interpreting typical large-error-sensitive mistakes. |
| **R²** | How much variation in the target the model explains compared with a simple baseline. | Comparing regression models in context. |

### Example: Delivery-Time Predictions

| Actual delivery time (minutes) | Prediction | Absolute error |
|---:|---:|---:|
| 110 | 100 | 10 |
| 120 | 125 | 5 |
| 90 | 95 | 5 |

```text
MAE = (10 + 5 + 5) / 3 = 6.7 minutes
```

The meaning depends on the task. An average error of 6.7 minutes may be acceptable for a broad delivery estimate but unacceptable for coordinating emergency services.

## Evaluate Generative AI with Task-Specific Criteria

Generative AI does not always have one correct answer. Evaluation can combine automated checks with human review using a clear rubric.

### Example: Customer-Support Assistant Rubric

For each test conversation, reviewers can score:

| Criterion | Question |
|---|---|
| **Correctness** | Is the answer factually correct and consistent with the approved policy? |
| **Relevance** | Does it answer the customer’s actual question? |
| **Completeness** | Does it include the information needed to act? |
| **Safety** | Does it avoid harmful, private, or unsupported instructions? |
| **Tone** | Is it clear, respectful, and appropriate? |
| **Escalation** | Does it ask for human help when it should? |

```text
Test request: "Can I change the delivery address after shipment?"

Good answer: explains the approved policy, states any limits,
and directs the customer to human support when an exception is needed.
```

The test set should include ordinary requests, ambiguous cases, edge cases, and attempts to make the assistant ignore its rules.

## Inspect Errors, Not Only Scores

Metrics show whether a model is improving, but error analysis explains why it fails.

### Example: Review Missed Spam

Suppose many false negatives contain image-only advertisements. That suggests the text-based spam model cannot see the relevant information. Possible responses include adding an image-analysis component, routing image-heavy messages to review, or deciding that the use case needs a different approach.

Useful questions during error analysis:

- Which examples fail most often?
- Do failures cluster by input type, language, date, or user group?
- Are labels wrong or ambiguous?
- Does the model fail when it is highly confident or when it is uncertain?
- Are mistakes acceptable for the people affected?

## Evaluate Fairness and Safety

Overall average performance can hide poor results for some groups or important cases. Evaluate relevant slices of the data separately.

### Example: Voice Transcription

A speech-to-text system may have good overall word accuracy but work less well for certain accents, background-noise levels, or microphones. Evaluate these cases separately before claiming that the model is ready for everyone.

Also test safety boundaries. For example, a customer-support assistant should not expose account information, invent a refund policy, or make promises it cannot keep.

## Evaluate After Release

Evaluation continues after deployment because users, data, and conditions change.

```text
Before release: offline test set and human review
After release: monitor real outcomes, errors, feedback, and changing data
```

### Example: Data Drift

A spam model trained last year may slowly become less effective as senders change their wording and tactics. Monitor false positives, missed spam, user reports, and changes in the input data. Update the model or its rules when evidence shows performance has declined.

## An Evaluation Checklist

- Define the task, intended users, and cost of each error.
- Use training, validation, and test data for their separate purposes.
- Ensure evaluation data resembles real-world use, including edge cases.
- Choose metrics that match the task and error costs.
- Inspect the confusion matrix for classification, not only accuracy.
- Set decision thresholds deliberately.
- Review individual errors and data slices.
- Include human review or rubrics when outputs are open-ended.
- Test privacy, fairness, safety, and security requirements.
- Monitor real-world outcomes after release.

## Key Takeaways

- Evaluate models on unseen data that represents real use.
- A useful metric depends on the task and the cost of mistakes.
- Accuracy alone can be misleading, especially for rare events.
- Confusion matrices, precision, recall, and thresholds reveal classification tradeoffs.
- ROC curves and AUC compare a classifier’s ranking performance across thresholds.
- Micro, macro, and weighted averages summarize multi-class results differently; always inspect per-class performance.
- Regression models need numerical-error metrics such as MAE or RMSE.
- Generative AI benefits from structured human rubrics and adversarial test cases.
- Evaluation is continuous: inspect errors, test safety and fairness, and monitor after release.

## References

- [Google Machine Learning Crash Course: Accuracy, precision, recall, and related metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) — free explanations of classification metrics and their tradeoffs.
- [Google Machine Learning Crash Course: Thresholds and the confusion matrix](https://developers.google.com/machine-learning/crash-course/classification/thresholding) — free introduction to decision thresholds and classification outcomes.
- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) — documentation for classification, regression, clustering, and other evaluation metrics.
