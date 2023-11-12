Postmortem: Datarefill.com.ng hosting webserver Outage Incident

Issue Summary:
Duration:
    	Start Time: August 15 2023, 22:39WAT
    	End Time: August 17, 2023, 01:45WAT

Impact:
The outage affected the website data refill and other website hosted as an addon account to the primary stellar plus web server. 
Users experienced a 100% increase in latency, with intermittent errors and  and user account been declared suspended
Approximately 100% of users were affected during the peak of the incident.
Root Cause:
The root cause of the outage was identified as an unexpected surge in traffic which led to using more resources than was allocated to each add-on account. 

Timeline:
Detection:
Start Time: August 15 2023, 22:39 WAT
: The issue was initially detected through automated monitoring alerts indicating a hosting suspension error and latency.
Engineers also received reports from users experiencing slow page loading times.
Actions Taken:
Investigation started with a focus on the web servers and database clusters to identify any potential issues.
Assumptions were initially made about increased database load due to recent code deployments.
Misleading Investigation: Early focus on database-related issues led to unnecessary optimization efforts on the database servers.
Escalation:
 August 15 2023, 22:39WAT: Incident escalated to the infrastructure team as the web server logs did not reveal any significant issues.
Additional teams were brought in to assess network configurations and potential DDoS attacks.
Resolution:
August 17, 2023, 01:45WAT: The root cause was finally traced to the use of more resources allocated to the stellar plus hosting account purchased.
Load balancer settings were promptly corrected, and normal traffic distribution was restored.
Latency and error rates returned to baseline within 15 minutes of the resolution.

Corrective and Preventative Measures:
Improvements/Fixes:
Enhance load testing procedures to simulate and prepare for sudden traffic spikes.
Implement stricter change management policies for critical infrastructure components like load balancers.
Improve monitoring systems to provide more detailed insights into load balancer performance.
Tasks to Address the Issue:
Conduct a comprehensive review of load balancer configurations to identify and rectify potential misconfigurations.
Develop and implement a thorough incident response plan for similar issues in the future.
Enhance collaboration and communication channels between development, infrastructure, and operations teams to expedite issue resolution.
Conclusion:
The outage on August 15 2023, 22:39WAT, served as a valuable learning experience. By addressing the root cause promptly and implementing corrective measures, we aim to fortify our system against similar incidents in the future. This postmortem underscores the importance of continuous monitoring, effective collaboration, and rigorous testing in maintaining the reliability and performance of our web stack.

