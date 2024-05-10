import AnchorJS from 'anchor-js';

let anchorJSInstance = AnchorJS;

export const setAnchorJS = (value) => {
  anchorJSInstance = value;
};

export default anchorJSInstance;
