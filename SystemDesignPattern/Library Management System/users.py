#Account, Member, and Librarian: These classes represent various people that interact with our system:

from abc import ABC
from datetime import datetime
from constants import *

class Account(ABC):
    def __init__(self, name, aadhar_num, contact_info):
        self._name = name
        self._aadhar_num = aadhar_num
        self._contact = contact_info
        self._password = "abcd"  # Default password
        self._doj = datetime.now()  # Date of joining

    @abstractmethod
    def update_profile(self, data_to_update):
        """
        Abstract method to be implemented by subclasses. Will handle profile updates.
        """
        pass

    def check_id_exists(self, id):
        """
        Check if the member/librarian ID exists in the members table.
        This is a high-level method to be implemented, actual DB logic not needed for LLD.
        """
        pass

    def forgot_password(self, id, new_password):
        """
        Allows users to reset their password if they exist in the system.
        """
        if self.check_id_exists(id):
            # Logic to update the password in the database
            # High-level flow: update password, log reset time, and notify user
            return "Password reset successfully."
        return "User ID not found."


class Member(Account):
    def __init__(self, name, aadhar_num, contact_info):
        super().__init__(name, aadhar_num, contact_info)
        self.is_verified = False  # Members need to verify critical details like Aadhar

    def update_profile(self, data_to_update):
        """
        Member-specific profile update logic. Handles profile updates, including Aadhar validation.
        """
        if ACCOUNT_CREATION_VALIDATION_COL[0] in data_to_update:
            # If the profile update includes Aadhar, flag for admin approval
            data_to_update["is_admin_verified"] = AdminApproval.PENDING
            # High-level explanation: send notification to admin, prevent transactions until verified.
        # Logic to update other profile information (contact, profile picture, etc.)
        return "Profile updated, pending admin approval for critical changes."

    def renew_membership(self):
        """
        Allows members to renew their library membership.
        Key logic: renew within allowed time frame (e.g., 10 days before/3 days after expiry).
        """
        current_date = datetime.now()
        if self.is_in_renewal_period(current_date):
            # Renew the membership by extending expiry date and processing payment
            # High-level flow: update subscription date, increment renewal count
            return "Membership renewed successfully."
        return "Renewal window has closed."

    def is_in_renewal_period(self, current_date):
        """
        Placeholder function for checking whether the member is within the allowed renewal window.
        """
        pass


class Librarian(Account):
    def __init__(self, name, aadhar_num, contact_info):
        super().__init__(name, aadhar_num, contact_info)

    def update_profile(self, data_to_update):
        """
        Librarian updates his profile. Does not need aadhar validation as he is the admin.
        """
        # Logic to update other profile information (contact, profile picture, etc.)
        return "Profile updated, pending admin approval for critical changes."
    
           

    

