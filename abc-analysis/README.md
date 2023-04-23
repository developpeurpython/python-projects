# Introduction

As a data analyst, I was tasked with conducting a case study on a dataset containing information about summer products with their ratings and performance. The purpose of this case study is to analyze and understand the performance of various products in terms of revenue generation, and to classify these products into categories using the ABC classification method. This case study aims to demonstrate the applicability of data analysis techniques in addressing real-world challenges faced by businesses when making decisions related to product offerings and inventory management. The dataset used in this case study can be found at the following link: https://github.com/amankharwal/Website-data/blob/master/summer-products-with-rating-and-performance_2020-08.csv. The dataset contains information such as product title, price, units sold, and user ratings.

# Problems

The major problem identified in this case study is determining the revenue performance of various summer products and classifying them into meaningful categories. To analyze this problem, I have used descriptive statistics, data visualization techniques, and clustering algorithms to extract valuable insights from the dataset and to support my findings with facts.

# Solutions

To address the problem, I have implemented the following solution:

- Analyze the dataset using descriptive statistics and data visualization techniques to understand the overall performance of the products.
- Calculate the revenue for each product and categorize them into revenue bins.
- Apply the K-Means clustering algorithm to classify the products into three distinct categories based on their revenue distribution.
- Assign the ABC classification to each product based on the K-Means clustering results.
- Analyze the distribution of products and revenue across the ABC categories.

This solution provides a systematic approach to classify the products based on their revenue performance. The pros of this solution include the ability to identify high-performing products and their contribution to the total revenue. The cons of this solution include the assumptions made during the clustering process, which might not accurately represent the real-world distribution of product categories.

Below are some visualizations:

- **Distribution of Products in ABC Categories:** 

This visualization helps in understanding the proportion of products in each category and identifying the most common and least common categories. The x-axis represents the ABC categories, while the y-axis represents the number of products. The percentages above the bars indicate the proportion of products in each category relative to the total number of products.

This visualization reveals that the majority of the products fall under category C, followed by categories B and A. This indicates that most products have lower revenue generation, while a smaller proportion of products have higher revenue generation.

![image](https://user-images.githubusercontent.com/115745200/233815641-f761b916-6aee-468d-89fe-735c7d7c3b42.png)

- **Revenue Distribution by ABC Categories:**

This visualization helps in understanding the contribution of each category to the overall revenue. The x-axis represents the ABC categories, and the y-axis represents the total revenue generated by products in each category. The percentages above the bars indicate the proportion of revenue contributed by each category relative to the total revenue.

This visualization shows that the A category products contribute the most to the overall revenue, followed by the B and C category products. This suggests that focusing on the A category products can significantly improve the overall revenue performance of the business.

![image](https://user-images.githubusercontent.com/115745200/233815646-68a68c4b-33d2-42ae-bbee-3ddfe4b31206.png)

- **Average Revenue by ABC Categories:**

This visualization helps in understanding the average revenue performance of products in each category. The x-axis represents the ABC categories, and the y-axis represents the average revenue generated by products in each category.

This visualization highlights that the A category products generate the highest average revenue, followed by the B and C category products. This further emphasizes the importance of focusing on the A category products to maximize revenue generation.

![image](https://user-images.githubusercontent.com/115745200/233815649-52c9a25c-d40d-46ae-952d-c193392bace2.png)

# Conclusion

Through the case study, I have successfully analyzed the summer products dataset and identified the revenue performance of various products. By applying the K-Means clustering algorithm, I was able to classify the products into the ABC categories and understand the distribution of products and revenue across these categories. The insights gained from this analysis can help businesses make informed decisions regarding product offerings and inventory management.

# Next steps

Based on the analysis, I recommend that the business should focus on the products in the A category, as they generate the highest revenue. The company should invest resources in promoting and maintaining adequate inventory levels for these high-performing products to maximize revenue. The B category products should also be monitored and evaluated for potential improvements or adjustments in marketing strategies. The C category products should be re-evaluated to determine if they are still viable in the current market or if they should be discontinued or replaced with more profitable offerings. These recommendations should be implemented by the relevant departments within the company and monitored closely to assess their effectiveness in improving the overall revenue performance.