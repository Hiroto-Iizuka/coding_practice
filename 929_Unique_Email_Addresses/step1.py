from collections import defaultdict

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = collections.defaultdict(int)

        for email in emails:
            local_name, _, domain_name = email.partition("@")

            local_name = local_name.partition("+")[0]
            local_name = local_name.replace(".", "")

            normalized = f"{local_name}@{domain_name}"
            unique_emails[normalized] += 1

        return len(unique_emails)