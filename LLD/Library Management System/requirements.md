## Version - I - LMS

- There are 3 actors - System, Librarian and Member.

### Librarian:
- The librarian acts as the admin for the system
- Operations the user can perform wrt to Books:
    - Add books using following information - Book Title, Rack, Publisher, Publication Date, Author Name,Book Item,Book Status,book format
    - Search books using Title, Author, Publisher,Book Id
    - Update Book Items, book status
    - Soft Delete the book and book items if book is lost
    - View the list of books available in LMS. Filter by genre,status,author,publisher
- Operations the user can perform wrt to Members:
    - Add Member Information includes - Member Name, Aadhar Number, Date of Joining, Profile Pic - involves payment operation
    - Search member information using Name,Aadhar Number, DoJ
    - Update Member Information
    - Soft Delete Member Information if member did not renew LMS subscription or wanted to leave LMS
    - View the list of members part of LMS
    - Approve the member post validation
- Operations the user can perform wrt to Books and Members:
    - Issue book to member
    - Re-enter the book information in LMS upon return by Member, involves updating the book item
    - Collect the fine when a book is lost by user - involves payment operation
    - View books alloted to each member - includes returned,nearing due date, currently issued books and lost books by user
    - Extend the book membership for user post due date

### System:
- The system usually does the background work here
- Notify the Member about the LMS subscription renewal 30,15,10 days prior if not renewed by then
- Notify the Member about the due date to return the book 10 days prior & after due date is passed (if due date is not extended)
- Notify the Librarian about the due date to return the books
- Limit the librarian & member to issue only 5 books/month - block further issuance
- Notify user when unavailable book is now available
- Limit the librarian & member to extend the due date by 2 weeks
- Limit the LMS subscription renewal by 1 year
- Autogenerate unique book-id and member-id (specify prefix ID format for ebooks & hardcopies)
- Set the due date for issued book - 10 days
- Collect fines for books retunred after due date
- For ebooks allow only LMS members access
- Fine for lost books will be (MRP/book + Rs.100)
- Notify the admin if the user has uploaded any verification doc and until admin approved don't allow the user to do any operation.

### Library Member:
- The Member is the main user of the system
- Operations the user can perform:
    - View the list of books available in LMS & their status
    - Search books using Title,Author,Publisher,BookId
    - Self checkout books (ebooks only, hardcopies need to be done at counter)
    - Modify the member profile information - for critical information submit the proof - such as Aadhar Number Update
    - View books(hardcopies & ebooks) taken by the member and its status - when was it returned, currently due, fined books (any books on which fine was levied because it was lost). Filter by genre,status,author,publisher
    - Pay the fine for the book misplaced / retunred after due date
    - Request for due date extension - for hardcopies
    - Renew LMS subscription
    - Bookmark unavailable books (limited to harcopies)
