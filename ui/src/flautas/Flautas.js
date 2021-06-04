import "./Flautas.css";
import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";
import GridLayout from "react-grid-layout";
import ContentEditable from "react-contenteditable";
import { useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";
import Editor from "react-simple-code-editor";
import { highlight, languages } from "prismjs/components/prism-core";

function highlightWords(string) {
    string = string.replace(/<[^>]*>?/gm, "");

    string = string.replace(
        /((class|declaration statement|function|annotation))/g,
        `<span class="hl-italic">$1</span>`
    );

    string = string.replace(
        /((must have))/g,
        `<span class="hl-blue-bg">$1</span>`
    );
    let set = new Set();
    for (let item of string.match(/("[a-zA-Z]+")/g)) {
        set.add(item);
    }
    for (let item of set) {
        string = string.replaceAll(item, `<span class="hl-red">${item}</span>`);
    }
    return string;
}

function Flautas() {
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

    const [cursorPos, setCursorPosition] = useState(null);

    const [html, setHtml] = useState(
        `class with (annotation "Path" ) must have (annotation "RegisterRestClient" and declaration statement with (annotation "Inject" and annotation "Claim" ) and function with (annotation "Path" and annotation "Produces" and annotation "GET" and annotation "Traced" ) )`
    );

    const handleChange = (evt) => {
        setCursorPosition(evt.target.selectionStart);
        setHtml(evt.target.value);
    };

    const handleFocus = (evt) => {
        if (cursorPos != null) {
            evt.target.selectionStart = cursorPos;
        }
    };

    const updateLayout = (key) => {
        const a = layout.filter((obj) => obj.i !== key);
        setLayout(a);
    };

    const checkIfExists = (key) => {
        return layout.some((obj) => obj.i === key);
    };

    const [code, setCode] = useState(`@Path(value="dummy-value")
@RegisterRestClient
class DemoClass {

    @Inject
    @Claim
    private Object field;

    @Path
    @Produces
    @GET
    @Traced
    public Object method() {}
}`);

    const compliant = `@Path(value="demo")
@RegisterRestClient
public class Correct {

    @Inject
    @Claim
    private String field;

    @Path
    @Produces
    @GET
    @Traced
    public void method(){}

}`;

    const nonCompliant = `@Path(value="demo")
@RegisterRestClient
public class Incorrect {

    @Inject
    @Claim
    private String field;

    @Path
    @Produces
    @GET
    /* Missing: @Traced */
    public void method(){}

}`;

    return (
        <div className="flautas">
            <div className="code-example">
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
                                    <button onClick={() => updateLayout("b")}>
                                        X
                                    </button>
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
                                        <button
                                            onClick={() => updateLayout("f")}
                                        >
                                            X
                                        </button>
                                    </div>
                                ) : (
                                    <></>
                                )}

                                {checkIfExists("k") ? (
                                    <div className="a annotation" key="k">
                                        <p>@Claim</p>
                                        <button
                                            onClick={() => updateLayout("k")}
                                        >
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
                                cols={4}
                                rowHeight={10}
                                width={1100}
                            >
                                {checkIfExists("h1") ? (
                                    <div className="a annotation" key="h1">
                                        <p>@Path</p>
                                        <button
                                            onClick={() => updateLayout("h1")}
                                        >
                                            X
                                        </button>
                                    </div>
                                ) : (
                                    <></>
                                )}

                                {checkIfExists("h2") ? (
                                    <div className="a annotation" key="h2">
                                        <p>@Produces</p>
                                        <button
                                            onClick={() => updateLayout("h2")}
                                        >
                                            X
                                        </button>
                                    </div>
                                ) : (
                                    <></>
                                )}

                                {checkIfExists("h3") ? (
                                    <div className="a annotation" key="h3">
                                        <p>@GET</p>
                                        <button
                                            onClick={() => updateLayout("h3")}
                                        >
                                            X
                                        </button>
                                    </div>
                                ) : (
                                    <></>
                                )}

                                {checkIfExists("h4") ? (
                                    <div className="a annotation" key="h4">
                                        <p>@Traced</p>
                                        <button
                                            onClick={() => updateLayout("h4")}
                                        >
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
                <div className="code-snippet-sidebar">
                    <Editor
                        value={code}
                        onValueChange={(code) => setCode(code)}
                        highlight={(code) => highlight(code, languages.java)}
                        padding={10}
                        style={{
                            fontFamily: '"Fira code", "Fira Mono", monospace',
                        }}
                        className="code-snippet-textbar"
                    />
                </div>
            </div>

            <div className="code-desc-container">
                <div className="code-description">
                    <ContentEditable
                        html={highlightWords(html)}
                        disabled={false}
                        onChange={handleChange}
                        onFocus={handleFocus}
                        className="code-description-text"
                    />
                </div>
                <div className="code-snippet-examples">
                    <div className="correct">
                        <h1>Compliant</h1>
                        <Editor
                            value={compliant}
                            onValueChange={(code) => setCode(code)}
                            highlight={(code) =>
                                highlight(code, languages.java)
                            }
                            padding={10}
                            style={{
                                fontFamily:
                                    '"Fira code", "Fira Mono", monospace',
                            }}
                            className="code-snippet-textbar"
                        />
                    </div>
                    <div className="violation">
                        <h1>Non-compliant</h1>
                        <Editor
                            value={nonCompliant}
                            onValueChange={(code) => setCode(code)}
                            highlight={(code) =>
                                highlight(code, languages.java)
                            }
                            padding={10}
                            style={{
                                fontFamily:
                                    '"Fira code", "Fira Mono", monospace',
                            }}
                            className="code-snippet-textbar"
                        />
                    </div>
                </div>
                <div className="controls">
                    <div className="left-btn-div">
                        <button className="btn-round btn-left">
                            <span>
                                <FaArrowLeft />
                            </span>
                        </button>
                    </div>

                    <div className="buttons">
                        <button className="btn btn-correct">CORRECT</button>
                        <button className="btn btn-corrected">
                            BEST PRACTICE
                        </button>
                        <button className="btn btn-incorrect">
                            NOT A RULE
                        </button>
                        {/* <button className="btn-round btn-right">
                            <span>
                                <FaCheck />
                            </span>
                        </button>
                        <button className="btn-round btn-right">
                            <span>
                                <FaHeart />
                            </span>
                        </button>
                        <button className="btn-round btn-left">
                            <span>
                                <FaTimes />
                            </span>
                        </button> */}
                    </div>

                    <div className="right-btn-div">
                        <button className="btn-round btn-right">
                            <span>
                                <FaArrowRight />
                            </span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Flautas;
