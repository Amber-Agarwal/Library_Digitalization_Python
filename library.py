from hash_table import HashMap
from hash_table import HashSet

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def merge_sort_tuples(self,word_index_tuples):
        if len(word_index_tuples) <= 1:
            return word_index_tuples

        mid = len(word_index_tuples) // 2
        left_half = self.merge_sort_tuples(word_index_tuples[:mid])
        right_half = self.merge_sort_tuples(word_index_tuples[mid:])

        return self.merge(left_half, right_half)

    def merge(self,left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:  # Compare the words
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Append any remaining elements from both halves
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list
    
    def merge_sort(self,words):
        if len(words) <= 1:
            return words

        mid = len(words) // 2
        left_half = self.merge_sort(words[:mid])
        right_half = self.merge_sort(words[mid:])

        return self.merge_words(left_half, right_half)

    def merge_words(self,left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:  # Lexicographical comparison
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Append any remaining elements from both halves
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

    def __init__(self, book_titles, texts):
        self.book_titles = book_titles
        new_book_titles = []
        for i in range(len(book_titles)):
            new_book_titles.append((book_titles[i],i))
        self.sorted_book_title_tuple = self.merge_sort_tuples(new_book_titles)
        self.sorted_text = [[] for i in range(len(texts))]
        for i in range(len(texts)):
            self.sorted_text[i] = self.merge_sort(texts[i])
        self.distinct_words_list = [[] for i in range(len(texts))]
        for i in range(len(texts)):
            self.distinct_words_list[i].append(self.sorted_text[i][0])
            for j in range(1,len(self.sorted_text[i])):
                if self.sorted_text[i][j]!=self.sorted_text[i][j-1]:
                    self.distinct_words_list[i].append(self.sorted_text[i][j])

    def my_binary_search(self,words, target):
        left, right = 0, len(words) - 1

        while left <= right:
            mid = (left + right) // 2
            word, index = words[mid]

            if word == target:
                return index  # Return the index of the found word
            elif word < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def words_binary_search(self,words,target):
        left, right = 0, len(words) - 1

        while left <= right:
            mid = (left + right) // 2
            word = words[mid]

            if word == target:
                return 1  # Return the index of the found word
            elif word < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
    def distinct_words(self, book_title):
        req_index = self.my_binary_search(self.sorted_book_title_tuple,book_title)
        return self.distinct_words_list[req_index]
    
    def count_distinct_words(self, book_title):
        req_index = self.my_binary_search(self.sorted_book_title_tuple,book_title)
        return len(self.distinct_words_list[req_index])
    
    def search_keyword(self, keyword):
        ans_list = []
        for i in range(len(self.sorted_book_title_tuple)):
            if self.words_binary_search(self.distinct_words_list[self.sorted_book_title_tuple[i][1]],keyword)==1:
                ans_list.append(self.sorted_book_title_tuple[i][0])
        return ans_list


    
    def print_books(self):
        for i in range(len(self.sorted_book_title_tuple)):
            book_title = self.sorted_book_title_tuple[i][0]
            book_index = self.sorted_book_title_tuple[i][1]
            output = ' | '.join(self.distinct_words_list[book_index])
            print(f"{book_title}: {output}")


class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name = name
        self.params = params
        if name == "Jobs":
            self.bookmap = HashMap("Chain",params)
        elif name == "Gates":
            self.bookmap = HashMap("Linear",params)
        elif name == "Bezos":
            self.bookmap = HashMap("Double",params)
        self.book_distinct_words = []
        self.added_books = []
    def add_book(self, book_title, text):
        self.added_books.append(book_title)
        wordset = HashSet(self.bookmap.collision_type,self.params)
        for i in range(len(text)):
            # if book_title == "GameOfThrones":
                # print(text[i])
            wordset.insert(text[i])
        self.bookmap.insert((book_title,wordset))
        if self.name == "Jobs":
            for entry in wordset.table:
                if entry is not None:
                    wordset.dist+=len(entry)
        else:
            for entry in wordset.table:
                if entry is not None:
                    wordset.dist += 1



    def distinct_words(self, book_title):
        required_word_set = self.bookmap.find(book_title)
        distinct_words = []
        if self.name == "Jobs":
            for entry in required_word_set.table:
                if entry is not None:
                    for sub_entry in entry:
                        distinct_words.append(sub_entry)
        else:
            for entry in required_word_set.table:
                if entry is not None:
                    word = entry
                    distinct_words.append(word)
        return distinct_words

    
    def count_distinct_words(self, book_title):
        required_word_set = self.bookmap.find(book_title)
        
        return required_word_set.dist

    def search_keyword(self, keyword):
        req_books = []
        
        for book in self.added_books:
            wordset = self.bookmap.find(book)
            if wordset.find(keyword):
                req_books.append(book)
        
        return req_books
    
    def print_books(self):
        # print(self.bookmap.table)
        # if self.name == "Jobs":
            for book in self.added_books:
                wordset = self.bookmap.find(book)
                # if book:
                #     for sub_book in book:
                #         if sub_book:
                #             title_of_the_book,wordset = sub_book
                #             required = "; ".join([str(word) for word in self.distinct_words(title_of_the_book)])
                print(f"{book}: {wordset.__str__()}")

        # else:
            # for book in self.bookmap.table:
                # if book:
                    # title_of_the_book,word_set = book
                    # required = "; ".join([str(word) for word in self.distinct_words(title_of_the_book)])
                    # print(f"{title_of_the_book}: {word_set.__str__()}")

# # # Initialize parameters for "Jobs" hashing strategy
# params_jobs = (35, 41)  # Example params, adjust according to your hash implementation
# jlib = JGBLibrary("Jobs", params_jobs)

# # Add books with some words
# jlib.add_book("Book", ["the", "quick", "brown", "fox"])
# jlib.add_book("Books", ["jumps", "the", "over", "the", "lazy", "dog"])
# jlib.add_book("GameOfThrones", ["winter", "is", "coming", "dragons", "kingdom", "war", "betrayal"])
# jlib.add_book("TheGreatGatsby", ["greatness", "dream", "money", "love", "parties", "mystery"])
# jlib.add_book("TheCatcherInTheRye", ["teenage", "rebellion", "innocence", "Salinger", "Holden", "NewYork", "alienation"])
# jlib.add_book("BraveNewWorld", ["the","utopia", "science", "society", "freedom", "individuality", "Huxley", "technology"])
# jlib.add_book("Fahrenheit", ["burning", "books", "freedom", "knowledge", "society", "censorship", "rebellion"])
# # print(jlib.bookmap.table)
# # Search for a keyword present in "Book1"
# # print(jlib.search_keyword("the"))  # Expected output: ["Book1"]
# # print(jlib.search_keyword("the"))
# # jlib.print_books()

# # book_titles = ["Booka", "Bookb", "Bookc"]
# # texts = [
# #     ["apple", "banana", "apple", "cherry", "date"],       # Distinct words: apple, banana, cherry, date
# #     ["banana", "fig", "grape", "fig", "apple"],           # Distinct words: banana, fig, grape, apple
# #     ["cherry", "banana", "apple", "grape", "banana"]      # Distinct words: cherry, banana, apple, grape
# # ]
# # params_jobs = [31, 11]        # Parameters for "Jobs" (z, initial_table_size)
# params_gates = [37, 13]       # Parameters for "Gates" (z, initial_table_size)
# params_bezos = [31, 37, 7, 11]  # Parameters for "Bezos" (z1, z2, c2, initial_table_size)

# # Testing JGBLibrary with "Jobs" collision handling (chaining)
# print("\nTesting JGBLibrary (Jobs)")
# josh_library = JGBLibrary("Jobs", params_jobs)
# josh_library.add_book("Booka", texts[0])
# josh_library.add_book("Bookb", texts[1])
# josh_library.add_book("Bookc", texts[2])

# # Check distinct words for a book
# print("\nDistinct words in Book1:")
# print(josh_library.distinct_words("Booka"))  # Expected output: List of distinct words in Book1

# # Check count of distinct words for a book
# print("\nCount of distinct words in Book2:")
# print(josh_library.count_distinct_words("Bookb"))  # Expected output: Count of distinct words in Book2

# # Check keyword search across books
# print("\nBooks containing the word 'grape':")
# print(josh_library.search_keyword("grape"))  # Expected output: List of book titles containing "grape"

# # Print all books and their distinct words
# print("\nAll books and their distinct words in JGBLibrary (Jobs):")
# josh_library.print_books()
