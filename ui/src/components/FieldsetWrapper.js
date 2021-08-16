function FieldsetWrapper(props) {
    const { title } = props;

    let legend = null;
    if (title.includes(":")) {
        const [editor, fileName] = title.split(":");
        legend = (
            <legend>
                <strong>{editor.trim()}</strong>: <em>{fileName.trim()}</em>
            </legend>
        );
    } else {
        legend = (
            <legend>
                <strong>{title}</strong>
            </legend>
        );
    }
    return (
        <fieldset>
            {legend}
            {props.children}
        </fieldset>
    );
}

export default FieldsetWrapper;
