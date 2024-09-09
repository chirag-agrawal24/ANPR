# Contributors:
  1. Chirag Agrawal - [Github](https://github.com/chirag-agrawal24) [LinkedIn](https://www.linkedin.com/in/-chirag-agrawal-/)
  2. Deepanshu Kesharwani - [Github](https://github.com/Dkesharwan) [LinkedIn](https://www.linkedin.com/in/deepanshu-kesharwani-0028b1191)



# Metrics:
1. YOLO Metrics
   ![image](https://github.com/user-attachments/assets/9a3b4893-a42d-4246-afb4-c7172d66ee95)

Primary Objective: Focus on enhancing the model's recall to maximize the detection of number 
plates from input frames. 
- Precision Management: Acceptable to have lower precision, as any background text detected can be 
filtered out during the text extraction process. 
- Recall-Confidence Analysis:
  * Lowering the confidence threshold improves recall, which is key for detecting more number 
plates. 
  * A very low confidence score, however, can lead to a significant reduction in precision. 
- Resource Utilization:
  * Excessively low confidence may increase false positives, leading to unnecessary use of 
computational resources. 
- Balanced Approach: It's important to optimize recall while carefully managing precision to avoid 
inefficiencies.
- At a confidence threshold of **25%** , the YOLOv8 model achieved the following 
performance metrics: a Recall of **88.62%**, a Precision of **95.61%**, and an F1 score of 
**91.98%**.
  
2. TrOCR Testing Metric
  * The Microsoft TrOCR model shines with an impressive overall accuracy of **95.61%**, showcasing its strong 
capabilities in general text recognition tasks. However, this prowess falters when the focus shifts to car 
number plates, where the accuracy notably drops to **71.56%**. This decline suggests that the intricacies of car 
plate recognition pose unique challenges, possibly due to varying fonts, plate designs, or environmental 
conditions.

  * The situation becomes more challenging with bike number plates, where the model's performance falls short entirely. It struggles to detect any characters, indicating a gap in its ability to handle the distinctive features of bike plates, such as their smaller size, non-standard formats, or different placement on the vehicle.

3. Speed:
- YOLOv8 Performance: 
  * Without GPU: The YOLOv8 model requires 146.7 milliseconds to detect a number plate. 
  * With GPU: When GPU acceleration is enabled, the detection time is significantly reduced to just 6.6 milliseconds. 
- Microsoft TrOCR Performance: 
  * The TrOCR model takes 578 milliseconds to generate results for text recognition. 

This data highlights the substantial impact of GPU utilization on the performance of YOLOv8, dramatically 
improving the speed of number plate detection. Meanwhile, the Microsoft TrOCR model, while effective in 
text recognition, requires a longer processing time
