# AWS Lambda (Amazon Web Services Lambda)

AWS Lambda is an event-driven computing cloud service from Amazon Web Services that allows developers to program functions on a pay-per-use basis without having to provision storage or compute resources to support them.

One of the main benefits of AWS Lambda is that it abstracts server management away from the IT professional. With AWS Lambda, Amazon manages the servers, which allows a developer to focus more on writing application code.

AWS supports code written in a variety of programming languages. AWS Lambda languages include Node.js, Python, Java and C#. Developers can also use code compiler tools, such as Maven or Gradle, and packages to build functions.

# AWS Lambda functions

A function is a small piece of programming that carries out a specific task. Developers use AWS Lambda to code and run functions in response to specific events in other Amazon cloud services, such as the creation of an object in an Amazon Simple Storage Service (S3) bucket. Each Lambda function runs in an isolated computing environment with its own resources and view of the file system.

When AWS Lambda functions are called, the storage and compute resources for that function spin up automatically as a metered service.

Developers can list, delete, update and monitor functions through the Lambda dashboard, command-line interface (CLI) or software development kit (SDK). The service also performs infrastructure-focused activities, such as server and operating system maintenance, patch deployment and logging through AWS CloudWatch. Lambda also supports third-party logging application programming interfaces (APIs), and developers can connect custom APIs to Lambda through the Amazon API Gateway service.

# AWS Lambda pricing and free tier

Amazon bills users based on the number of requests served and the compute time needed to run the code, metered in increments of 100 milliseconds. If a function is never called, it costs the developer nothing.


