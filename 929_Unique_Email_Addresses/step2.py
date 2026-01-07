class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local_name, domain_name, *rest = email.split("@")
            if rest:
                raise ValueError(f"There are two or more @ in {email}")

            local_name_normalized = local_name.replace(".", "").split("+")[0]
            unique_emails.add((local_name_normalized, domain_name))

        return len(unique_emails)
    