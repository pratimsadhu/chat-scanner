import re

def scan_file_for_keywords(file_path, keywords, buffer_size=3):
    relevant_lines = []
    lines = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    added_lines = set()

    # Helper function to determine if a line matches a keyword or sublist
    def matches_keyword(line, keyword):
        if isinstance(keyword, list): 
            return all(re.search(rf"\b{re.escape(kw)}\b", line, re.IGNORECASE) for kw in keyword)
        return re.search(rf"\b{re.escape(keyword)}\b", line, re.IGNORECASE)

    # Iterate through each line and check for matches
    for line_number in range(len(lines)):
        line = lines[line_number]
        if any(matches_keyword(line, keyword) for keyword in keywords):
            start_index = max(0, line_number - buffer_size)
            end_index = min(len(lines), line_number + buffer_size + 1)

            # Add lines from the range (with buffer)
            for i in range(start_index, end_index):
                line_to_add = (i + 1, lines[i].strip())
                if line_to_add not in added_lines:
                    relevant_lines.append(line_to_add)
                    added_lines.add(line_to_add) 

    return relevant_lines

def main():
    input_file_path = "input/chat.txt"
    keywords = [["pratim", "samyak", "shalom"]]
    output_file_path = f"output/{input_file_path.split('/')[-1]}"

    # Scan for relevant lines
    results = scan_file_for_keywords(input_file_path, keywords, buffer_size=0)

    # Write results to the output file, overwriting if it exists
    with open(output_file_path, "w") as file:
        for line_number, line in results:
            file.write(f"{line_number}: {line}\n")

if __name__ == "__main__":
    main()

