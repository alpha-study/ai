from django.core.management.base import BaseCommand, CommandError
from ai_chatbot.models import KnowledgeDocument
from ai_chatbot.tasks import process_document


class Command(BaseCommand):
    help = 'Enqueue reprocessing for a KnowledgeDocument or all documents.'

    def add_arguments(self, parser):
        parser.add_argument('--id', dest='doc_id', help='UUID of document to reprocess')
        parser.add_argument('--all', action='store_true', help='Reprocess all documents')

    def handle(self, *args, **options):
        doc_id = options.get('doc_id')
        do_all = options.get('all')
        if not doc_id and not do_all:
            raise CommandError('Provide --id <uuid> or --all')

        if do_all:
            qs = KnowledgeDocument.objects.all()
            for d in qs:
                process_document.delay(str(d.id))
            self.stdout.write(self.style.SUCCESS(f'Enqueued reprocessing for {qs.count()} documents'))
            return

        try:
            d = KnowledgeDocument.objects.get(id=doc_id)
        except KnowledgeDocument.DoesNotExist:
            raise CommandError('Document not found')

        process_document.delay(str(d.id))
        self.stdout.write(self.style.SUCCESS(f'Enqueued reprocessing for {d.id}'))
