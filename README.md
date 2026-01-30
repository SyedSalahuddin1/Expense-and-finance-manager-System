Expense & Finance Managment System (Python OOP)
📌Project Overview 
This project is a production-grade Python application designed to demonstrate Object-Oriented Programming (OOP), Clean Architecture, and SOLID principles through a real-world expense and account management system.

The system models financial accounts, expenses, and business workflows using encapsulation, inheritance, polymorphism, composition, abstraction, and design patterns.

This project is intentionally built phase-by-phase to reflect how real software systems evolve in industry. 

🧠Key Concepts Demonstrated 
* Object-Oriented Programming (OOP)
* Clean Architecture
* Domain-Driven Design (DDD – lightweight)
* SOLID Principles
* Dependency Injection
* Design Patterns (Factory, Strategy, Observer)
* Repository Pattern
* Unit Testing with Test Doubles
* Separation of Concerns
* Scalable & Maintainable Code Design

🏗️ Architecture Overview
The project follows Clean Architecture, ensuring that business rules are independent of frameworks and infrastructure.
domain/         → Core business logic (Entities, Value Objects)
services/       → Application use-cases
repositories/   → Data access abstractions & implementations
strategies/     → Pluggable business rules (Strategy Pattern)
factories/      → Centralized object creation (Factory Pattern)
observers/      → Event-driven extensions (Observer Pattern)
tests/          → Unit tests (Mocks, Fakes)
main.py         → Composition root / application entry point

🧩 Core Features 
* Create and manage mulitple account types
  *Savings Account
  *Credit Account
* Enforce business rules using encapsulation
* Apply expenses using interchangeable strategies
* Support credit limits and interest calculation
* Event notifications using observers
* Easily extensible without modifying existing code

  
🧱 OOP Principles Applied
* Encapsulation: State mutation is controlled via methods and properties
* Inheritance: Specialized account types extend a base Account class
* Polymorphism: Same interface, different behavior (e.g., withdrawal rules)
* Abstraction: Services and repositories depend on interfaces, not implementations
* Composition: Objects collaborate instead of relying on deep inheritance

🧠 SOLID Principles Compliance
-> S (SRP): Each class has a single responsibility
-> O (OCP): New features added without modifying existing code
-> L (LSP): Subclasses respect base class contracts
-> I (ISP): Interfaces are minimal and focused
-> D (DIP): High-level modules depend on abstractions

🧪 Testing Strategy
* Unit tests for domain logic and services
* Use of Fake objects and Mocks
* No dependency on databases or external services
* Tests validate behavior, not implementation details

  🛠️ Technologies Used
# Python 3.x
# Standard Library (abc, unittest)
# Object-Oriented Design Patterns
# Clean Architecture principles

🚀 How to Run
python main.py
TO Run tests 
pytest 


🎯 Why This Project Matters
** This project demonstrates:
** Strong understanding of software design
** Ability to build scalable systems
** Clean separation between business logic and infrastructure
** Industry-relevant OOP and architectural skills

It is Suitable for:
* Software Engineering Interviews
* Backend/ Python Developer roles
* Demonstrating system design thinking
* Portfolio and resume projects

👨‍💻 Author
Syed Salahuddin
Aspiring Software Engineer | Python Developer
Focused on writing clean, maintainable, and scalable software


📄 License
This project is for educational and portfolio purposes

