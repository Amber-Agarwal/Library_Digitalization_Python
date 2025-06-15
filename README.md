# Library Digitalization System

**Author:** Amber Agarwal  
**Course:** COL 106 - Data Structures and Algorithms  
**Institution:** Indian Institute of Technology Delhi  
**Instructor:** Professor Amit Kumar  
**Assignment:** Assignment 4 - Library Digitalization  
**Date:** October 2024

## 📚 Project Overview

This project implements a comprehensive library digitalization system for the IITD library, designed to digitize thousands of rare books, journals, and magazines. The system focuses on creating compressed dictionaries for individual books and enabling efficient keyword searches across the library's collection.

## 🎯 Problem Statement

The IITD library needed a solution to:
- Create compressed dictionaries containing only words present in specific books
- Enable keyword-based search functionality to find relevant books
- Analyze text content to find and count distinct words efficiently

## 🏗️ System Architecture

The project implements two distinct approaches through different "developers":

### 1. **Musk's Approach (2nd Year - MuskLibrary)**
- **Method:** Mergesort-based solution
- **Strategy:** Sort all words and extract unique words through traversal
- **Output:** Lexicographically sorted distinct words

### 2. **JGB Approach (4th Year - JGBLibrary)**
- **Method:** Hash Table-based solutions with different collision handling
- **Developers:**
  - **Jobs:** Chaining for collision resolution
  - **Gates:** Linear Probing for collision resolution
  - **Bezos:** Double Hashing for collision resolution

## 🔧 Core Components

### Hash Table Implementation

#### **Hash Functions**
1. **Primary Hash Function:** Polynomial Accumulation Hash
   ```
   h(s) = p(a₀) + p(a₁)z + p(a₂)z² + ... + p(aₙ)zⁿ
   ```
   Where p(a-z) = 0-25, p(A-Z) = 26-51

2. **Secondary Hash Function (Double Hashing):**
   ```
   h₂(s) = c₂ - ((p(a₀) + p(a₁)z + p(a₂)z² + ... + p(aₙ)zⁿ) mod c₂)
   ```

#### **Collision Resolution Methods**
- **Chaining:** Uses linked lists to handle collisions
- **Linear Probing:** Sequential search for next available slot
- **Double Hashing:** Uses secondary hash function for step size

### Dynamic Resizing
- **Load Factor Threshold:** 50% (α ≥ 0.5)
- **Resizing Strategy:** Double the table size to next prime number
- **Rehashing:** All existing elements are rehashed into the new table

## 📁 File Structure

```
library-digitalization/
├── hash_table.py           # Base hash table implementations (HashSet, HashMap)
├── dynamic_hash_table.py   # Dynamic resizing hash tables
├── library.py              # Digital library implementations (MuskLibrary, JGBLibrary)
├── main.py                 # Testing and debugging script
├── prime_generator.py      # Prime number generation utility (provided)
└── README.md              # This file
```

## 🔍 Key Features

### Hash Table Classes
- **HashSet:** Stores unique keys
- **HashMap:** Stores key-value pairs
- **DynamicHashSet/DynamicHashMap:** Auto-resizing versions

### Core Operations
- `insert(x)`: Insert new element/pair
- `find(key)`: Search for key in table
- `get_slot(key)`: Get slot index for key
- `get_load()`: Calculate current load factor

### Digital Library Classes
- **MuskLibrary:** Mergesort-based word processing
- **JGBLibrary:** Hash table-based word processing

### Library Operations
- `distinct_words(book_title)`: Get unique words in a book
- `count_distinct_words(book_title)`: Count unique words
- `search_keyword(keyword)`: Find books containing keyword
- `print_books()`: Display all books with their distinct words

## ⚡ Performance Analysis

### MuskLibrary (Mergesort Approach)
- **Initialization:** O(kW log W) - k books, W words each
- **Distinct Words:** O(D + log k) - D distinct words
- **Count Distinct:** O(log k)
- **Keyword Search:** O(k log D)
- **Print Books:** O(kD)

### JGBLibrary (Hash Table Approach)
- **Initialization:** O(table_size)
- **Add Book:** O(W) - W words in book
- **Distinct Words:** O(D) - D distinct words
- **Count Distinct:** O(1)
- **Keyword Search:** O(k)
- **Print Books:** O(kD)

## 🛠️ Implementation Details

### Hash Table Features
- **Modular Design:** Base class with specialized child classes
- **Multiple Collision Handling:** Support for chaining, linear probing, and double hashing
- **Dynamic Resizing:** Automatic table expansion when load factor exceeds 50%
- **Custom Hash Functions:** Polynomial accumulation with mod compression

### String Formatting
- **Empty Slots:** `<EMPTY>`
- **Separators:** `|` between slots, `;` between chained elements
- **Format Examples:**
  - HashSet: `Stack | AVL | <EMPTY> | Heap | Hash`
  - HashMap: `(Stack, 1) | (AVL, 2) | <EMPTY> | (Heap, 3) | (Hash, 4)`

## 🧪 Testing

The `main.py` file contains test cases for:
- Hash table operations with different collision methods
- Dynamic resizing functionality
- Library operations for both MuskLibrary and JGBLibrary
- Performance comparison between different approaches

## 📋 Requirements & Constraints

- **No Built-in Data Structures:** Custom implementation required (no `set` or `dict`)
- **No External Libraries:** All functionality implemented from scratch
- **Time Complexity:** All operations must meet specified time requirements
- **Memory Efficiency:** Dynamic resizing for optimal space utilization

## 🚀 Usage Example

```python
# Initialize JGBLibrary with Jobs' chaining method
library = JGBLibrary("Jobs", (31, 7))

# Add books to library
library.add_book("Hamlet", ["to", "be", "or", "not", "to", "be"])
library.add_book("Macbeth", ["fair", "is", "foul", "and", "foul", "is", "fair"])

# Get distinct words
hamlet_words = library.distinct_words("Hamlet")
print(f"Hamlet distinct words: {hamlet_words}")

# Search for keyword
books_with_be = library.search_keyword("be")
print(f"Books containing 'be': {books_with_be}")

# Print all books
library.print_books()
```

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **Hash Table Design:** Understanding of different collision resolution strategies
- **Algorithm Analysis:** Comparing time and space complexities of different approaches
- **Dynamic Data Structures:** Implementation of auto-resizing hash tables
- **Object-Oriented Design:** Modular architecture with inheritance
- **Performance Optimization:** Balancing time and space efficiency

## 🏆 Academic Context

This assignment was part of the Data Structures and Algorithms course at IIT Delhi, focusing on:
- Advanced hash table implementations
- Collision resolution techniques
- Dynamic memory management
- Algorithm comparison and analysis
- Real-world application of theoretical concepts

---

*This project showcases the practical application of fundamental computer science concepts in solving real-world problems, specifically in the domain of digital library management and text processing.*
