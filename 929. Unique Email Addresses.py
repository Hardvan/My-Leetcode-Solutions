class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_emails = []
        for email in emails:
            lst = email.split("@")
            first = lst[0]
            last = lst[-1]
            first = first.replace(".","") # Removing .
            # Removing word after +
            first = first.split("+")[0]
            em = f"{first}@{last}"
            final_emails.append(em)
        
        return len(set(final_emails))
