import deepl

auth_key = "# Replace with your key"
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="JA")
print(result.text) 

# print("Source languages:")
# for language in translator.get_source_languages():
#     print(f"{language.name} ({language.code})")  # Example: "German (DE)"

# print("Target languages:")
# for language in translator.get_target_languages():
#     if language.supports_formality:
#         print(f"{language.name} ({language.code}) supports formality")
#         # Example: "Italian (IT) supports formality"
#     else:
#         print(f"{language.name} ({language.code})")
#         # Example: "Lithuanian (LT)"