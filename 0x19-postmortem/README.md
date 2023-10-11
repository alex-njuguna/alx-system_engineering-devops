

Issue Summary:
Duration: October 10, 2023, 17:30 - 19:45 (EAT)
Impact: The web service threw a little temper tantrum, leading to a 45% reduction in user capacity. Users had a roller-coaster ride with slow page loads and surprise errors.
Root Cause: It turns out our database had stage fright and forgot its lines, a missing index left it speechless.
Timeline:
17:30 (EAT): The web service pulled a "Houdini" act as engineers received multiple monitoring alerts for increased latency.
Actions: Engineers initiated a digital detective escapade, reviewing system logs, performance metrics, and network activity. They initially thought it was a traffic jam slowing things down.
Misleading Paths: Like searching for your keys under a lamppost, the team looked into network configurations and imagined DDoS dragons. No mysteries were solved.
Escalation: The incident was bumped up to the senior DevOps team, now grappling with a tech thriller.
18:15 (EAT): The plot twist was that a missing database index was the main character causing the commotion.
Root Cause: A database query had a dramatic pause due to the missing index, making it the prime suspect in our technological whodunit.
Resolution: At 18:45 (EAT), our heroic engineers applied a magical hotfix, finally getting that index on stage.
Service Recovery: By 19:45 (EAT), the web service took a final bow, and the users enjoyed a standing ovation.

Corrective and Preventative Measures:
Improvements: Our script for success includes:
Comprehensive Monitoring: Setting up a backstage alert system for database query performance.
Regular Code Review: Enforcing code review practices to catch any missing "actors" in the database queries.
Automated Testing: Introducing automated tests to rehearse for performance issues before showtime.
Tasks: The show must go on! Here's our to-do list:
Develop a Playbook: Creating an incident response playbook to ensure future acts run smoothly.
Review Database Schemas: Regularly reviewing our database's script to spot any missing characters and tune query performance.
Conduct a Post-Incident Review: Learning from the "Great Glitch of 2023" and enhancing future incident handling.
Implement Automated Index Creation: Ensuring that our databases have all the right actors in their cast, automatically.


Conclusion: The "Great Glitch of 2023" was quite the show, with a missing database index playing the star role. After approximately 2 hours and 15 minutes of high drama, we're stepping up our game with enhanced monitoring, code review, and testing processes, along with automated index creation. We apologize for the suspense and thank our team for their swift response in bringing the curtain down on this unexpected performance.


