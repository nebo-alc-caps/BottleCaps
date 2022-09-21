from square_connection import SquareConnection
from square_catalog import VariationPricingType, CatalogBatchUpsertRequest, CatalogObjectBatch, CatalogObjectItem, CatalogObjectVariation, SquareCatalog
from square_catalog import FixedPrice, VariationPrice


if __name__ == "__main__":
    conn = SquareConnection.get_default_sandbox()
    cata = SquareCatalog(conn)

    var = CatalogObjectVariation("#test_var", "Little Test", VariationPrice(FixedPrice(100)))

    item = CatalogObjectItem("#test", "Test", [var])

    batch = CatalogObjectBatch([item])

    cata.register_new(item)
    cata.register_new(var)

    cata.batch_upsert(CatalogBatchUpsertRequest([batch]))
