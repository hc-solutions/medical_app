import * as React from "react";

type SuperProps = {
    payload: String
}


const SuperComponent: React.FC<SuperProps> = ({ payload }) => {
    return (
        <div className="super-container">
            {payload}
        </div>
    )
}

export default SuperComponent
