from .tag_creator_controller import TagCreateController

def test_create():
    mock_value = "image_path"
    tag_creator_controller = TagCreateController()

    result = tag_creator_controller.create(mock_value)
    print(result)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]
