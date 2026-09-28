# Adds an `ics` metadata entry (<slug>.ics) to every talk that does not set
# one, before rendering, so the talk layout links to the calendar file that
# .github/scripts/generate_ics.py writes for every talk.
Jekyll::Hooks.register :talks, :pre_render do |doc|
  doc.data["ics"] ||= "#{File.basename(doc.path, '.*')}.ics"
end
