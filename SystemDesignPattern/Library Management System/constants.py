from enum import Enum

class BookFormat(Enum):
    EBOOKS = 1
    HARDCOPY = 2

class BookStatus(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 2
    ISSUED = 3
    MISPLACED = 4
    RETURNED =5
    DUE_SOON = 6

class MembershipStatus(Enum):
    ACTIVE =1
    CLOSED = 2
    CANCELLED =3
    BLACKLISTED =4
    PENDING = 5

class Genre(Enum):
    COMIC = 1
    EDUCATION =2
    GK =3
    NOVEL =4
    FANTANSY =5

class AdminApproval(Enum):
    PENDING =1
    APPROVED =2
    REJECTED =3

class UserRole(Enum):
    ADMIN =1
    MEMBER=2

class Constants():
    def __init__(self) -> None:
        self.MAX_BOOKS_ISSUED_TO_A_USER = 5
        self.MAX_LENDING_DAYS = 10
        self.SUBSCRIPTION_RENEWAL_TIME = 12
        self.DUE_DATE_EXTENSION = 14
        self.SUBSCRIPTION_RENEWAL_FEE = 1000

ACCOUNT_CREATION_VALIDATION_COL = ["aadhar_file_url"]