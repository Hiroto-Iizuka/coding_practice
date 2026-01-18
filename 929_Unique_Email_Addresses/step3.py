class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails: set[tuple[str, str]] = set()

        for email in emails:
            split_result = email.split("@")
            if len(split_result) != 2:
                raise ValueError(f"email address '{email}' must contain only one @")
            local_name, domain_name = split_result

            local_name_deleted_dot = local_name.replace(".", "")
            local_name_normalized = local_name_deleted_dot.split("+", maxsplit=1)[0]
            unique_emails.add((local_name_normalized, domain_name))

        return len(unique_emails)
    