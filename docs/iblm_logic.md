# IBLM (Interaction-Based Learning Model) Logic

The IBLM uses a combination of **Frustration (F)** and **Stimulus Value (SVI)** to determine content difficulty.

- **Frustration Score (F)**: Calculated based on rapid skips or negative sentiment.
- **SVI (Stimulus Value Index)**: Calculated based on duration of engagement and positive text feedback.

### Adaptation Rules
- If **F > 0.7**: Trigger "Empathy Mode" (simplify content immediately).
- If **SVI > 0.8**: Trigger "Challenge Mode" (introduce advanced sub-topics).
