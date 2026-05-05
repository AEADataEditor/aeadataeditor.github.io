# Adds per-collection `future` support. If a collection defines `future: true`
# in its collections config, future-dated documents in that collection are
# published regardless of the global `future` setting.
module Jekyll
  class Publisher
    def hidden_in_the_future?(document)
      future = if document.respond_to?(:collection) && document.collection
                 document.collection.metadata.fetch("future", site.future)
               else
                 site.future
               end
      !future && document.respond_to?(:date) && document.date.to_i > site.time.to_i
    end
  end
end
