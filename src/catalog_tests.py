from square_connection import SquareConnection
from square_catalog import CatalogBatchUpsertRequest, CatalogObjectBatch, CatalogObjectItem, CatalogObjectVariation, SquareCatalog

if __name__ == "__main__":
    conn = SquareConnection.get_default_sandbox()
    cata = SquareCatalog(conn)

    var = CatalogObjectVariation("#test_var", "Little Test")

    item = CatalogObjectItem("#test", "Test", [var])

    batch = CatalogObjectBatch([item])

    cata.batch_upsert(CatalogBatchUpsertRequest(batch))
