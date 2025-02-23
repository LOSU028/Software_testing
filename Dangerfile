max_title_length = 50

danger.git.commits.each do |commit|
  title = commit.message.lines.first.strip # Extracts the first line (title)
  if title.length > max_title_length
    fail("The commit title is too long (#{title.length} characters). Please keep it under #{max_title_length} characters.")
  end
end
