max_title_length = 50
min_description_length = 5
max_line_length = 72

git.commits.each do |commit|
  message_lines = commit.message.lines.map(&:strip) # Get all lines
  title = message_lines.first # First line is the title
  description_lines = message_lines[1..] || [] # Everything after title

  # Check title length
  if title.length > max_title_length
    fail("The commit title is too long (#{title.length} characters). Keep it under #{max_title_length} characters.")
  end

  # Check empty line between title and description
  if description_lines.any? && description_lines.first != ""
    fail("The commit message must have an empty line between the title and description.")
  end

  # Remove first empty line to get the actual description
  actual_description = description_lines.drop(1)

  # Check description length
  if actual_description.any? && actual_description.join.length < min_description_length
    fail("The commit description must have at least #{min_description_length} characters.")
  end

  # Check line length in the description
  long_lines = actual_description.select { |line| line.length > max_line_length }
  if long_lines.any?
    fail("Each line in the commit description must be at most #{max_line_length} characters. Found #{long_lines.map(&:length).join(', ')} characters long lines.")
  end
end
