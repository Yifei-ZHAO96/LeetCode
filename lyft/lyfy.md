# Business case
## 给CEO准备dashboard 如何选metrics
   
**Ride Volume and Growth**

- Total Rides: The total number of rides completed over a specific period.

- Monthly Active Riders (MAR): The number of unique riders who used the service within a month.

- Ride Growth Rate: The percentage increase in ride volume compared to previous periods.

Why: These metrics indicate the overall demand for Lyft's services and the company's market penetration.

**Revenue Metrics**

- Total Revenue: The total income generated from rides.
- Revenue per Ride: Average revenue generated per ride.
- Revenue Growth Rate: The percentage increase in revenue over time.

**Cost and Efficiency Metrics**

- Cost per Ride: Average cost incurred per ride.
- Driver Earnings: Average earnings per driver.
- Operational Costs.

**Customer Satisfaction and Retention**

- Net Promoter Score (NPS): Measures customer loyalty and satisfaction.
- Customer Retention Rate: Percentage of riders who return to use the service.
- Average Rating: Average rider rating given by customers.

**Market Penetration and Expansion**

- Geographic Distribution of Rides: Breakdown of rides by city or region.
- New Market Entries: Number of new cities or regions where Lyft has launched services.
- Market Share: Comparison with key competitors in various regions.

**Driver Metrics**

- Driver Retention Rate: Percentage of drivers who continue to work with Lyft over time.
- Driver Satisfaction Score: Measures drivers' contentment with the platform.
- Driver Onboarding Rate: Number of new drivers joining the platform.

**Technology and Innovation**

- App Performance Metrics: App load time, crash rate, and user engagement metrics.
- Feature Adoption Rate: Percentage of users adopting new features (e.g., ride-sharing options, payment methods).
- R&D Spend: Investment in research and development.

## Define/predict available drivers

### Define Available Drivers
Available drivers are those who are currently logged into the app, not engaged in a ride, and ready to accept new ride requests. The key factors influencing driver availability include:

- Time of Day: Peak hours (e.g., morning and evening commutes) vs. off-peak hours.
- Day of Week: Weekdays vs. weekends.
Location: Urban areas vs. suburban or rural areas.
- Driver Preferences: Individual driver preferences for working hours and locations.
- External Factors: Weather conditions, local events, holidays, etc, regulations.

### Data Collection
Collect historical data that includes:

- Driver Status Logs: Timestamped records of when drivers log in, log out, accept rides, and complete rides.
- Ride Request Logs: Timestamped records of ride requests and completions.
- Driver Profiles: Information about driver activity patterns, preferred working hours, and locations.
- External Data: Weather conditions, local events, traffic conditions, and holidays.

### Feature Engineering
Create features that can help predict driver availability:

- Temporal Features: Hour of the day, day of the week, month, season.
- Geospatial Features: Location coordinates, city/region identifiers.
- Driver Behavior Features: Average number of rides per day, average shift length, historical availability patterns.
- External Features: Weather conditions (temperature, precipitation), event schedules (concerts, sports events).

### Model Selection
- Neural Networks: LSTM (Long Short-Term Memory) networks for capturing sequential patterns in time-series data.

### Model Training and Validation
Train the selected models using historical data:

- Split Data: Use techniques like cross-validation to split data into training and testing sets.
- Train Models: Fit the models to the training data, optimizing for performance metrics such as Mean - Absolute Error (MAE) or Root Mean Squared Error (RMSE).
- Validate Models: Evaluate model performance on the testing set, ensuring they generalize well to unseen data.

## 假如我们要launch a shared ride, what metrics would you look at to understand the health of the product?
### Driver side
i. Total hours on shared-ride mode (supply)
ii. Percentage of shared-ride mode hours / total active hours - – which reflects the driver’s willingness in turning on this option
iii. Average income per mile (compared with average income per mile for non-shared ride)
iv. Route overlapping ratio
v. Average extra miles/minutes drove compared with if single ride route

### Rider side
i. Total number of requests for shared ride
ii. Percentage of shared-ride requests / total requests
iii. Cancellation rate (ETA is too high?)
iv. Average price paid per rider per mile (or per minutes)
v. Retention rate (use shared rider again after first time, or switched to more expensive single rider options)
vi. Average number of intermediate stops before reaching destination per passenger

## Decide which city to launch a service similar to Uber Eats, such as New York, San Francisco, or Chicago

### Market Demand and Competition
- Market Demand: Assess the demand for food delivery services in each city through market research and data analysis. High demand can be correlated with population density, consumer habits, and the development of the local restaurant industry.
- Competition: Evaluate the existing food delivery services and their market share in each city. Choosing a city with high demand but less competition can increase the chances of success.
### Population and Population Density
- New York: New York has one of the highest population densities in the U.S., offering a large potential user base. High density implies shorter delivery routes, enhancing delivery efficiency.
- San Francisco: Although less densely populated than New York, San Francisco's tech-savvy population and high-income levels make it an attractive market.
- Chicago: Chicago is the third-largest city in the U.S. with a large and evenly distributed population, offering significant market potential.
### Consumer Habits and Income Levels
- New York: New Yorkers have diverse consumer habits and a high demand for food delivery services. Higher income levels mean residents are more likely to use these services frequently.
- San Francisco: With generally high incomes and a tech-centric population, San Franciscans are likely to adopt new services quickly, making it a promising market.
- Chicago: While income levels are slightly lower, Chicago has a substantial middle class and professional workforce with steady demand for food delivery.
### Infrastructure and Logistics Capabilities
- New York: Despite complex traffic conditions, New York has a well-established logistics and delivery network that can support extensive food delivery services.
- San Francisco: With a smaller area and relatively good traffic conditions, San Francisco is conducive to quick and efficient food delivery.
- Chicago: Chicago's traffic conditions are moderate, and its strong logistics infrastructure makes it suitable for large-scale delivery services.
### Brand Visibility and Market Penetration
- New York: As the largest city, New York offers significant brand exposure and marketing opportunities. Success in New York can set a strong precedent for expanding to other cities.
- San Francisco: As a hub for technology and innovation, launching in San Francisco can attract media attention and early adopters, boosting the brand's innovative image.
- Chicago: Chicago's large market size and stable environment make it a reliable testing ground for new services.
### Conclusion
Considering these factors, New York might be the best city to launch a service similar to Uber Eats. Here’s why:

- High Demand and Population Density: New York’s high population density and diverse consumer demand allow for quick market validation of the new service.
- Established Logistics Network: Despite complex traffic, New York’s robust logistics infrastructure can support large-scale food delivery.
- Brand Exposure and Market Influence: Success in New York can provide significant brand exposure and a strong foundation for expansion to other cities.

## ETA增加了3min，怎么分析?
### Supply
i. Decreasing number of available drivers (short supply)
### Demand
i. Increasing demand (driven by lower price-> high conversion rate)
### Lyft – company side/ systematic error
- Map-matching issue (map has errors that caused inaccurate estimate)
  - Wrongly locate the driver (GPS)
  - Not reflecting the traffic condition
  - Current road condition is not factored in
  - Traffic lights or stop signs are ignored
  - Weather conditions are not considered
- Dispatch issue (not dispatching the nearest available driver)
- The app is experiencing legacy caused driver reacts slower than it used to be.

## 如何评估driver(or rider)的experience? 哪些metrics?
### Driver Experience Metrics
- Working Conditions and Earnings
Earnings per Hour: Measures the average income drivers earn per hour.
  - Acceptance Rate: The proportion of ride requests that drivers accept.
  - Completion Rate: The percentage of accepted rides that are completed by drivers.
  - Working Hours and Duration: The total number of hours drivers work per week and the distribution of their working hours.
- Satisfaction and Loyalty
  - Driver Satisfaction Score: Collected through surveys or in-app feedback.
  - Driver Churn Rate: The percentage of drivers who stop working for the platform within a specific period.
  - Driver Net Promoter Score (NPS): The likelihood of drivers recommending the platform to others.
- Safety and Support
  - Incident Rate: The number of incidents or accidents per thousand or ten thousand rides.
  - Safety Training and Support: The availability and utilization of safety training programs and support services for drivers.
### Rider Experience Metrics
- Service Quality
   - Average Wait Time: The average time from when a ride request is made to when the driver arrives.
   - Trip Duration: The actual time taken for trips compared to the estimated time.
   - Cancellation Rate: The percentage of ride requests that are canceled by either the rider or the driver.
- Satisfaction and Loyalty
  - Rider Satisfaction Score: Collected through in-app ratings or surveys.
  - Rider Net Promoter Score (NPS): The likelihood of riders recommending the platform to others.
  - Repeat Usage Rate: The percentage of riders who use the service multiple times within a specific period.
- Safety and Support
  - Safety Rating: Riders' ratings of drivers' safe driving practices.
  - Support Response Time: The time it takes for customer support to respond to rider feedback or complaints.

## 如果给1million dollar的marketing budget，请问如果分配在driver和rider上？

### Driver Acquisition and Retention: Ensure there are enough drivers to meet rider demand, reduce wait times, and improve service availability.
- Acquisition
  - Referral Programs
  - Digital Advertising
  - Local Events and Partnerships
- Retention and Engagement
  - Incentive Programs
  - Driver Support and Training
  - Community Building

### Rider Acquisition and Retention: Increase the number of users, enhance user experience, and drive more ride requests.
- Acquisition
  - Referral Programs
  - Digital Advertising
  - Promotion
- Retention and Engagement
  - Loyalty Programs
  - User Experience Improvements
  - Feedback and Improvement Initiatives

## Driver 突然变少 (under supply)了，你作为一个DS, 该肿么办？
### Identify and Analyze the Problem
- Data Collection:

  - Driver Activity Logs: Collect data on driver logins, ride acceptances, cancellations, and working hours.
  - Rider Demand Data: Collect data on ride requests, peak times, and unfulfilled ride requests.
  - Feedback Data: Gather feedback from drivers and riders to understand their pain points.

- Data Analysis:

  - Supply-Demand Gap: Identify patterns and times when the demand for rides exceeds the supply of drivers.
  - Geographic Analysis: Determine if the undersupply is location-specific.
  - Driver Churn Rate: Analyze the rate at which drivers leave the platform and potential reasons behind it.
### Predictive Modeling
- Demand Forecasting:

  - Time Series Analysis: Use models like ARIMA, SARIMA, or Prophet to forecast rider demand at different times and locations.
  - Seasonality and Trend Analysis: Incorporate seasonal patterns and trends to predict peak demand periods.
- Driver Availability Prediction:

  - Classification Models: Use machine learning models (e.g., Random Forest, XGBoost) to predict driver availability based on historical data and features such as time of day, day of the week, weather conditions, and local events.
  - Driver Behavior Analysis: Identify drivers likely to be available during peak times and target them with specific incentives.
### Optimization and Incentive Strategies
- Dynamic Pricing:

  - Implement surge pricing to incentivize drivers to work during peak demand times. Use reinforcement learning algorithms to dynamically adjust prices based on real-time supply and demand.
- Targeted Incentives:

  - Bonuses and Rewards: Offer bonuses for drivers who work during undersupplied times or in high-demand areas.
  - Guaranteed Earnings: Provide guaranteed earnings for drivers to reduce the risk of idle time.
- Shift Scheduling:

  - Predictive Scheduling: Use predictive models to suggest optimal working hours for drivers to maximize their earnings and meet demand.
  - Flexibility Programs: Implement flexible scheduling options to attract more part-time drivers.
### Driver Recruitment and Retention
- Recruitment
- Retention
### Real-Time Monitoring and Adjustment
- Real-Time Dashboard:

  - Develop a real-time dashboard to monitor driver supply and demand metrics, driver activity, and ride fulfillment rates.
  - Alert Systems: Implement alerts for when driver supply falls below certain thresholds, triggering automatic responses such as increased incentives or surge pricing.
- Continuous Improvement:

  - A/B Testing: Test different incentive and pricing strategies to determine their effectiveness.
  - Iterative Model Training: Continuously update predictive models with new data to improve accuracy and responsiveness.

## demand increases, what should we do? Funnel analysis from registration to becoming an active drive
### Comprehensive Metrics for Each Stage
- Awareness:

  - Impressions: Number of times ads are shown.
  - Click-through Rate (CTR): Percentage of ad views that result in clicks.
  - Sign-ups: Number of users who sign up after seeing the ad.
- Registration:

  - Registration Completion Rate: Percentage of users who complete the registration process.
  - Drop-off Rate: Percentage of users who abandon the registration process.
  - Average Registration Time: Time taken to complete registration.
- Verification:

  - Document Submission Rate: Percentage of users who submit the required documents.
  - Verification Success Rate: Percentage of users who pass the background check.
  - Verification Time: Average time to complete the background check.
- Training:

  - Training Completion Rate: Percentage of users who complete the training.
  - Engagement Rate: Percentage of users actively engaging with training materials.
  - Average Training Duration: Time taken to complete training.
- Vehicle Inspection:

  - Inspection Completion Rate: Percentage of users who complete the vehicle inspection.
  - Inspection Time: Average time to complete the vehicle inspection.
  - No-show Rate: Percentage of users who miss scheduled inspections.
- Activation:

  - Activation Rate: Percentage of users who complete their first ride.
  - Time to First Ride: Average time from registration to first ride.
  - First-ride Completion Rate: Percentage of drivers who successfully complete their first ride.
- Solutions to Address Drop-offs
  - Enhance Communication:

    Provide clear and timely updates throughout each stage of the funnel.
  - Use automated emails, SMS, and in-app notifications to keep prospective drivers informed.
- Optimize User Experience:

  - Simplify forms and processes to reduce friction.
  - Offer user-friendly interfaces and step-by-step guides.
- Provide Support:

  - Offer live chat, phone support, and FAQs to assist drivers at each stage.
  - Implement chatbot assistance for quick and efficient help.
- Incentivize Participation:

  - Provide financial incentives for completing key stages such as registration, training, and the first ride.
  - Offer referral bonuses to current drivers who bring new drivers to the platform.
- Monitor and Iterate:

  - Continuously track metrics and identify bottlenecks.
  - Regularly update and improve processes based on data-driven insights and feedback.

## Given a list of riders and a list of drives, what metrics could be used to match them? How to optimize your method?
