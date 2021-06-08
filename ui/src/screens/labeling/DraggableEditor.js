import "./DraggableEditor.css";
import { useState } from "react";
import GridLayout from "react-grid-layout";

function DraggableEditor() {

    const [layout, setLayout] = useState([
        { i: "a", x: 0, y: 0, w: 1, h: 2, isResizable: false, static: true },
        { i: "b", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "c", x: 0, y: 0, w: 1, h: 2, isResizable: false },

        { i: "d", x: 0, y: 0, w: 1, h: 2, isResizable: false, static: true },
        { i: "e", x: 1, y: 0, w: 1, h: 2, isResizable: false, static: true },

        { i: "f", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "k", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "g", x: 0, y: 0, w: 1, h: 2, isResizable: false },

        { i: "h1", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "h2", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "h3", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "h4", x: 0, y: 0, w: 1, h: 2, isResizable: false },
        { i: "i", x: 0, y: 0, w: 1, h: 2, isResizable: false },
    ]);

    const updateLayout = (key) => {
        const a = layout.filter((obj) => obj.i !== key);
        setLayout(a);
    };

    const checkIfExists = (key) => {
        return layout.some((obj) => obj.i === key);
    };

    return (
        <div className="dragged-area">
            <div className="draggable">
                <GridLayout
                    className="annotations"
                    layout={layout}
                    cols={4}
                    rowHeight={7}
                    width={1100}
                >
                    {checkIfExists("a") ? (
                        <div className="a annotation static" key="a">
                            <p>@Path(value="dummy-value")</p>
                        </div>
                    ) : (
                        <></>
                    )}

                    {checkIfExists("b") ? (
                        <div className="a annotation" key="b">
                            <p>@RegisterRestClient</p>
                            <button onClick={() => updateLayout("b")}>X</button>
                        </div>
                    ) : (
                        <></>
                    )}
                </GridLayout>

                <GridLayout
                    className="class"
                    layout={layout}
                    cols={4}
                    rowHeight={10}
                    width={1100}
                >
                    <div className="a static" key="d">
                        class DemoClass
                    </div>
                </GridLayout>

                <div className="declarations">
                    <GridLayout
                        className="field"
                        layout={layout}
                        cols={4}
                        rowHeight={10}
                        width={1100}
                    >
                        {checkIfExists("f") ? (
                            <div className="a annotation" key="f">
                                <p>@Inject</p>
                                <button onClick={() => updateLayout("f")}>
                                    X
                                </button>
                            </div>
                        ) : (
                            <></>
                        )}

                        {checkIfExists("k") ? (
                            <div className="a annotation" key="k">
                                <p>@Claim</p>
                                <button onClick={() => updateLayout("k")}>
                                    X
                                </button>
                            </div>
                        ) : (
                            <></>
                        )}
                        <div className="a static" key="g">
                            private Object field;
                        </div>
                    </GridLayout>
                </div>

                <div className="methods">
                    <GridLayout
                        className="method"
                        layout={layout}
                        cols={3}
                        rowHeight={10}
                        width={1100}
                    >
                        {checkIfExists("h1") ? (
                            <div className="a annotation" key="h1">
                                <p>@Path</p>
                                <button onClick={() => updateLayout("h1")}>
                                    X
                                </button>
                            </div>
                        ) : (
                            <></>
                        )}

                        {checkIfExists("h2") ? (
                            <div className="a annotation" key="h2">
                                <p>@Produces</p>
                                <button onClick={() => updateLayout("h2")}>
                                    X
                                </button>
                            </div>
                        ) : (
                            <></>
                        )}

                        {checkIfExists("h3") ? (
                            <div className="a annotation" key="h3">
                                <p>@GET</p>
                                <button onClick={() => updateLayout("h3")}>
                                    X
                                </button>
                            </div>
                        ) : (
                            <></>
                        )}

                        {checkIfExists("h4") ? (
                            <div className="a annotation" key="h4">
                                <p>@Traced</p>
                                <button onClick={() => updateLayout("h4")}>
                                    X
                                </button>
                            </div>
                        ) : (
                            <></>
                        )}

                        <div className="a static" key="i">
                            {"public String method() {}"}
                        </div>
                    </GridLayout>
                </div>
            </div>
        </div>
    );
}

export default DraggableEditor;